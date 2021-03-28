#Libarys
import sys
#Project
from res.config import VERSION_KEY

def as_client():
    if VERSION_KEY == "dev":
        print(f"Starte als Client")

def as_server():
    if VERSION_KEY == "dev":
        print(f"Starte als Server")


if __name__ == "__main__":
    if VERSION_KEY == "dev":
        print(f"Argumente gefunden : {len(sys.argv)}")
    if len(sys.argv) > 1:
        if sys.argv[1] == "server":
            as_server()
        else:
            as_client()
    else:
        #Default Clientanwendung
        as_client()