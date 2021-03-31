#Libarys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#Project
from res.logging import logging
import client.ui.mainframe as mainframe

#Global Vars
TAG = "CLIENT"
log = logging(TAG)

def main(name1, name2, name3, name4):
    app = QtWidgets.QApplication([])
    Dialog = QtWidgets.QDialog()
    ui = mainframe.Ui_Dialog()
    ui.setupUi(Dialog)
    ui.btnStatus1.setText(name1)
    ui.btnStatus2.setText(name2)
    ui.btnStatus3.setText(name3)
    ui.btnStatus4.setText(name4)
    Dialog.show()
    sys.exit(app.exec_())

def start(ip, port):
    try: 
        main("Kommen", "Gehen", "Pause Beginn", "Pause Ende")
    except Exception as e:
        log.log(str(e), 4)