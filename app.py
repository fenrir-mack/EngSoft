from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "meu nome é Gustavo RA: 10436455"
