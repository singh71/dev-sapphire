from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
from datetime import datetime
from urllib.parse import parse_qs

class ContactFormHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_POST(self):
        if self.path == '/api/contact':
            # Read the form data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse JSON data
                data = json.loads(post_data.decode('utf-8'))
                
                # Add timestamp
                data['received_at'] = datetime.now().isoformat()
                
                # Save to file (in production, use database)
                os.makedirs('contact_submissions', exist_ok=True)
                filename = f"contact_submissions/contact_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                
                # Send email (optional - implement with SMTP)
                # send_email_notification(data)
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                response = {
                    'success': True,
                    'message': 'Thank you! We will contact you soon.',
                    'data': data
                }
                
                self.wfile.write(json.dumps(response).encode())
                
                print(f"✓ Contact form submitted: {data['name']} ({data['email']})")
                
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'message': 'Invalid JSON'}).encode())
            
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'message': str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_GET(self):
        # Serve static files
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ContactFormHandler)
    print(f'''
╔════════════════════════════════════════════════════╗
║   DevSapphire Technologies Website Server         ║
╚════════════════════════════════════════════════════╝

✓ Server running on: http://localhost:{port}
✓ Contact API: http://localhost:{port}/api/contact
✓ Press Ctrl+C to stop

Serving files from: {os.getcwd()}
    ''')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n✓ Server stopped')
        httpd.server_close()

if __name__ == '__main__':
    run_server()
