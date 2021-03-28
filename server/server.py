#Libarys
from flask import Flask, url_for, render_template
#Project
from res.logging import logging
from res.config import VERSION, VERSION_KEY

#Global Vars
TAG = "SERVER"
log = logging(TAG)
app = Flask(__name__)

#Routen
@app.route("/")
def index():
    return render_template("index.html", version=VERSION, key=VERSION_KEY)

#Starte WebServer, Aufruf von main
def start(ip, port):
    log.log("API wird gestartet", 1)
    app.run(host=ip, port=port, debug=True)