# import threading
from core.user.client.connection import create_connection
import sys

# def receive(socket, signal):
#     while signal:
#         try:
#             data = socket.recv(32)
#             print(str(data.decode("utf-8")))
#         except:
#             print("You have been disconnected from the server")
#             signal = False
#             break


def run_client():
    host = 'localhost'
    port = 6784
    sock = create_connection((host, port))

    # Send data to server
    # str.encode is used to turn the string message into bytes so it can be sent across the network
    try:
        while True:
            message = input()
            sock.sendall(str.encode(message))
    except (KeyboardInterrupt, EOFError):
        sock.close()
        sys.exit(0)