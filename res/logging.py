#Libarys
#Project
from res.config import LOG_FILE, LOG_LEVEL, LOG_LVL_CONS, LOG_LVL_FILE

class logging():

    def __init__(self, tag):
        self.tag = tag.upper()

    def _get_date(self):
        return "20210328_12:00:00"

    def log(self, msg, prio):
        ts = self._get_date()
        #TODO Error Handling prio pruefen
        note = f"{ts} : {self.tag} : {LOG_LEVEL[prio]} : {msg}"

        if(prio >= LOG_LVL_CONS):
            print(note)
        if(prio >= LOG_LVL_FILE):
            file = open(LOG_FILE, "a", encoding="utf8")
            file.write(f"{note}\n")
            file.close()