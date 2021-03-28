#Libarys
import sys
#Project
from res.config import VERSION_KEY
from res.logging import logging

#Global Vars
TAG = "MAIN"
log = logging(TAG)

def as_client():
    log.log(f"Starte als Client", 0)

def as_server():
    log.log(f"Starte als Server", 0)

def cli():
    log.log(f"Starte CLI", 0)
    while True:
        cmd = input()        

if __name__ == "__main__":
    log.log("Programmstart", 1)    
    log.log(f"Argumente gefunden : {len(sys.argv)}", 0)
    if len(sys.argv) > 1:
        if sys.argv[1] == "server":
            as_server()
        else:
            as_client()
    else:
        #Default Clientanwendung
        as_client()

    cli()
else:
    log.log("Kann nicht Importiert werden", 4)