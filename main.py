#Libarys
import sys
import threading
#Project
from res.config import VERSION_KEY, SERVER_IP, SERVER_PORT
from res.logging import logging
from server import server
from client import client

#Global Vars
TAG = "MAIN"
log = logging(TAG)

def as_client(ip, port):
    log.log(f"Starte als Client", 0)
    client.start(ip, port)

def as_server(ip, port):
    log.log(f"Starte als Server", 0)
    server.start(ip, port)

def cli(mode):
    log.log(f"Starte CLI", 0)
    while True:
        cmd = input()   

if __name__ == "__main__":
    log.log("Programmstart", 1)    
    log.log(f"Argumente gefunden : {len(sys.argv)}", 0)

    mode = "client"
    if sys.argv[1] == "server":
            mode = "server"

    if len(sys.argv) > 2: #ARG3 IP
        SERVER_IP = sys.argv[2]
    if len(sys.argv) > 3: #ARG4 IP
        SERVER_PORT = int(sys.argv[3])

    log.log(f"Netzwerk Konfig : {SERVER_IP}:{SERVER_PORT}", 0)
    if mode == "server":
        as_server(SERVER_IP, SERVER_PORT)
    else:
        as_client(SERVER_IP, SERVER_PORT)

    cli(mode)
else:
    log.log("Kann nicht Importiert werden", 4)