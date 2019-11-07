import socket
import settings
from core.utils import log
from core.user.server.connection import new_connections


def run_server():
    # Get host and port
    host = settings.SERVER_HOST
    port = settings.SERVER_PORT

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    log("Server started on host %s and port %s" % (host, port))
    sock.listen(5)
    new_connections(sock)
    # Create new thread to wait for connections
    # new_connections_thread = threading.Thread(target=new_connections, args=(sock,))
    # new_connections_thread.start()
