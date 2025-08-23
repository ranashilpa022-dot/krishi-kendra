document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // page reload hone se rokta hai

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    fetch("http://127.0.0.1:5000/contact", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name, email, message })
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message);  // ye alert show karega
      })
      .catch(err => console.error("Error:", err));
  });
});

