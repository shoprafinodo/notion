from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return "Username and password are required.", 400
        return f"User {escape(username)} signed up successfully!", 201
    return "Please sign up by POSTing a username and password."


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return "Username and password are required.", 400
        return f"User {escape(username)} signed in successfully!", 200
    return "Please sign in by POSTing a username and password."


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        if not email:
            return "Email is required.", 400
        # Always return a generic response so the endpoint does not reveal
        # whether an account exists for the given email (avoids user enumeration).
        return "If an account exists for that email, a reset link has been sent.", 200
    return "Please request a password reset by POSTing an email."


if __name__ == "__main__":
    app.run()
