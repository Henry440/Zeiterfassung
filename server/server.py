#Libarys
from flask import Flask
#Project
from res.logging import logging

#Global Vars
TAG = "SERVER"
log = logging(TAG)
app = Flask(__name__)

@app.route("/")
def index():
    return("Hello World")

def start(ip, port):
    app.run(host=ip, port=port, debug=True)