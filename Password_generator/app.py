from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form["length"])
        password = generate_password(length)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
