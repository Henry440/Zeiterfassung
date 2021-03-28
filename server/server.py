#Libarys
from flask import Flask, url_for, render_template
#Project
from res.logging import logging
from res.config import VERSION, VERSION_KEY
from server.database.db_handler import handler

#Global Vars
TAG = "SERVER"
log = logging(TAG)
app = Flask(__name__)
db = handler()

#Routen
@app.route("/")
def index():
    return render_template("index.html", version=VERSION, key=VERSION_KEY)

@app.route("/worktime/<int:user_id>/")
def worktime(user_id):
    user = db.get_user_by_id(user_id)
    username = user[1]
    return render_template("worktime.html", username=username)

#Starte WebServer, Aufruf von main
def start(ip, port):
    log.log("API wird gestartet", 1)
    if VERSION_KEY == "dev":
        app.run(host=ip, port=port, debug=True)
    else:
        app.run(host=ip, port=port, debug=False)