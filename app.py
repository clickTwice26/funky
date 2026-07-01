from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/hello")
def hello():
    name = request.args.get("name", "<img src=\"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuVSHCLGhllIzFvqt08pmOpX_1bD2-zO12iynALHoDb1qicCYCZErKas8&s\">")
    return f"Hello, {escape(name)}!"
    # return f"Hello, {name}!"

@app.route("/welcome/<username>")
def welcome(username):
    return f"Welcome, {escape(username)}!"

@app.route("/user/<uuid:user_uuid>")
def users_uuid(user_uuid):
    return f"Users uuid : {escape(user_uuid)}"

@app.route("/status")
def status():
    return {
        "status" : "ok"
    }

@app.route("/developers")
def developers():
    return "Shagato Chowdhury & Umme Munia"

