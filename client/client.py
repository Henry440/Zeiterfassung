#Libarys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
#Project
from res.logging import logging
from res.config import CLIENT_CONFIG
import client.ui.mainframe as mainframe

#Global Vars
TAG = "CLIENT"
log = logging(TAG)

def main(names):
    app = QtWidgets.QApplication([])
    Dialog = QtWidgets.QDialog()
    ui = mainframe.Ui_Dialog()
    ui.setupUi(Dialog)
    ui.btnStatus1.setText(names[0])
    ui.btnStatus2.setText(names[1])
    ui.btnStatus3.setText(names[2])
    ui.btnStatus4.setText(names[3])
    Dialog.show()
    sys.exit(app.exec_())

def start(ip, port):
    names = []
    try: 
        with open(CLIENT_CONFIG) as json_file:
            data = json.load(json_file)
            for key in data["status_keys"]:
                names.append(data["status_keys"][key]["name"])
        main(names)

    except Exception as e:
        log.log(str(e), 4)