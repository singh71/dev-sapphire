# DevSapphire Technologies - HTML/CSS/JavaScript Website

## 📁 Files Structure
```
html-website/
├── index.html      # Main HTML file with all sections
├── style.css       # Complete styling with animations
├── script.js       # JavaScript for interactions
└── README.md       # This file
```

## 🚀 How to Use

### Method 1: Open Directly in Browser
1. Open `index.html` file in any web browser
2. That's it! No server required

### Method 2: Using Live Server
1. Install any local server (like Python's http.server)
2. Run: `python3 -m http.server 8000`
3. Open: http://localhost:8000

## 📋 Features

✅ **Fully Responsive** - Works on desktop, tablet, and mobile
✅ **Smooth Animations** - CSS animations and transitions
✅ **Portfolio Filtering** - Interactive project filtering
✅ **Contact Form** - Ready for backend integration
✅ **Smooth Scroll Navigation** - Seamless section scrolling
✅ **Mobile Menu** - Responsive hamburger menu
✅ **Modern Design** - Glass-morphism and gradient effects

## 🎨 Sections Included

1. **Header** - Fixed navigation with smooth scroll
2. **Hero** - Premium hero section with CTA buttons
3. **Services** - 6 service cards with hover effects
4. **Portfolio** - 6 projects with category filtering
5. **Testimonials** - 4 client testimonials
6. **Team/About** - 4 team members + company info
7. **Contact** - Contact form + company details
8. **Footer** - Complete footer with links

## 🔧 Backend Integration

To connect the contact form to backend:

1. Update `script.js` contact form handler
2. Uncomment the fetch API code
3. Add your backend endpoint URL
4. Handle form submission on server

Example API endpoint structure:
```javascript
POST /api/contact
Body: {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+91 98765 43210",
    "subject": "Project Inquiry",
    "message": "..."
}
```

## 🎯 Customization

### Change Colors
Edit CSS variables in `style.css`:
```css
:root {
    --primary-bg: #0a0f1e;
    --blue-primary: #3b82f6;
    --cyan: #06b6d4;
}
```

### Change Content
Edit text directly in `index.html`

### Add More Sections
Copy any section structure and modify

## 📱 Contact Information

- **Email**: 987kumarsinghkaran@gmail.com
- **Phone**: +91 98711 05093
- **Address**: Nangli Vihar, Najafgarh, New Delhi - 110043

## 🌟 Credits

Built with ❤️ using:
- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome Icons

---

**DevSapphire Technologies** - Crafting Digital Excellence
