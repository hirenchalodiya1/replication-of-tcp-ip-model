import socket
import sys
from core.utils import log


def create_connection(addr):
    host, port = addr
    # Attempt connection to server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return sock
    except (ValueError, OSError):
        log("Could not make a connection to the server\nQuitting")
        sys.exit(0)
