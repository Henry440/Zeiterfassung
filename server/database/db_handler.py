#Libarys
import sqlite3
#Project
from res.logging import logging
from res.config import DATABASE, DATABASE_DEV, VERSION_KEY

#Global Vars
TAG = "Database"
log = logging(TAG)

class handler():

    def _open_con(self):
        log.log("Verbinde zu Datenbank", 0)
        if VERSION_KEY == "dev":
            self.con = sqlite3.connect(DATABASE_DEV)
        else:
            self.con = sqlite3.connect(DATABASE)
        self.cur = self.con.cursor()

    def _close_con(self):
        log.log("Schließe Verbindung zu Datenbank", 0)
        self.cur.close()
        self.con.commit()
        self.con.close()

    def __init__(self):
        log.log("Inizialisiere Handler für Datenbank", 1)
