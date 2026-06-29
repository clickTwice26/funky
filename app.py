from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"



@app.route("/status")
def status():
    return {
        "status" : "ok"
    }

@app.route("/developers")
def developers():
    return "Shagato Chowdhury & Umme Munia"

