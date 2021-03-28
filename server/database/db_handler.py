#Libarys
import sqlite3
#Project
from res.logging import logging
from res.config import DATABASE, DATABASE_DEV, VERSION_KEY, DATABASE_TABLE_USER

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

    def get_user_by_id(self, id):
        log.log(f"Userabfrage {id}", 0)
        sql_return = self._sql_quarry(f"SELECT * FROM '{DATABASE_TABLE_USER}' WHERE id = {id}")
        print(sql_return)
        return sql_return[0]

    def _sql_quarry(self, quarry):
        self._open_con()
        ret = self.cur.execute(quarry)
        data = ret.fetchall()
        self._close_con()
        return data

    def __init__(self):
        log.log("Inizialisiere Handler für Datenbank", 1)
        
