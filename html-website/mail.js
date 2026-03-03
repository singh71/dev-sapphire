function sendMail() {

  let parms = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    phone: document.getElementById("phone").value,
    subject: document.getElementById("subject").value,
    message: document.getElementById("message").value
  };

  emailjs.send("service_upkj4s7", "template_0fcyw3c", parms)
  .then(function(response) {

      alert("Message sent successfully ✅");

      document.getElementById("contactForm").reset();

  }, function(error) {

      alert("Failed to send message ❌");

  });

}