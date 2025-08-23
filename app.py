from flask import Flask, request, jsonify
from flask_cors import CORS   # frontend aur backend connect karne ke liye

app = Flask(__name__)
CORS(app)

# Home Route
@app.route("/")
def home():
    return "🚀 Krishi Kendra Backend Running!"

# Contact Form ke liye API
@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # Abhi ke liye sirf console me print karenge
    print("📩 New Contact Message:")
    print(f"Name: {name}, Email: {email}, Message: {message}")

    return jsonify({"status": "success", "message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
