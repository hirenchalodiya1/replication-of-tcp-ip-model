import socket
from core.user.server.connection import new_connections


def run_server():
    # Get host and port
    host = "localhost"
    port = 6784

    # Create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)
    new_connections(sock)
    # Create new thread to wait for connections
    # new_connections_thread = threading.Thread(target=new_connections, args=(sock,))
    # new_connections_thread.start()
