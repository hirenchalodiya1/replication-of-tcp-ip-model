# import threading
from core.user.client.connection import create_connection
from core.middleware.str2byte import str2bytes
from core.middleware.checks.crc import CRC
from core.middleware.encode_decode import encode, decode
import sys


# Function used at the sender side to encode data
def apply_check_encoding(data):
    return CRC(data).encode()


def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(decode(data))
        except:
            print("You have been disconnected from the server")
            signal = False
            break


def run_client():
    host = 'localhost'
    port = 6784
    sock = create_connection((host, port))

    # Send data to server
    # str.encode is used to turn the string message into bytes so it can be sent across the network
    try:
        while True:
            # Input data to send
            input_string = input("Enter data you want to send: ")

            # Convert input data to byte form
            byte_message = str2bytes(input_string)
            print("Data in bytes form:", byte_message)

            # Encoded data
            enc_data = apply_check_encoding(byte_message)

            # Function to corrupt the data
            # enc_data = "101010"

            print("Encoded Data in bytes form:", enc_data)

            # Send the input data
            sock.sendall(encode(enc_data))

            # receive data from the server
            recv_data = sock.recv(1024)
            print(("Received message from the server: " + decode(recv_data)))

    except (KeyboardInterrupt, EOFError):
        sock.close()
        sys.exit(0)
