#Libarys
import sys
#Project
from res.config import VERSION_KEY, SERVER_IP, SERVER_PORT
from res.logging import logging

#Global Vars
TAG = "MAIN"
log = logging(TAG)

def as_client(ip, port):
    log.log(f"Starte als Client", 0)

def as_server(ip, port):
    log.log(f"Starte als Server", 0)

def cli():
    log.log(f"Starte CLI", 0)
    while True:
        cmd = input()   

if __name__ == "__main__":
    log.log("Programmstart", 1)    
    log.log(f"Argumente gefunden : {len(sys.argv)}", 0)
    if len(sys.argv) > 1: #ARG1 .\main.py | ARG2 server/client
        if len(sys.argv) > 2: #ARG3 IP
            SERVER_IP = sys.argv[2]
        if len(sys.argv) > 3: #ARG4 IP
            SERVER_PORT = int(sys.argv[3])

        log.log(f"Netzwerk Konfig : {SERVER_IP}:{SERVER_PORT}", 0)
        if sys.argv[1] == "server":
            as_server(SERVER_IP, SERVER_PORT)
        else:
            as_client(SERVER_IP, SERVER_PORT)
    else:
        #Default Clientanwendung
        log.log(f"Netzwerk Konfig : {SERVER_IP}:{SERVER_PORT}", 0)
        as_client(SERVER_IP, SERVER_PORT)

    cli()
else:
    log.log("Kann nicht Importiert werden", 4)