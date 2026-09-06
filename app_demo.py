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


if __name__ == "__main__":
    app.run()
