# import threading
from core.user.client.connection import create_connection
from core.middleware.checks.crc import CRC
from core.utils.str_byte_conversion import str2bytes, bytes2str, str2bits
import sys


# Function used at the sender side to encode data
def apply_check_encoding(data):
    return CRC(data).encode()


def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(bytes2str(data))
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
            inp_str_as_bits = str2bits(input_string)
            print("Data in bytes form:", inp_str_as_bits)

            # Encoded data
            enc_data = apply_check_encoding(inp_str_as_bits)

            # Function to corrupt the data
            # enc_data = "101010"

            print("Encoded Data in bytes form:", enc_data)

            # Send the input data
            sock.sendall(str2bytes(enc_data))

            # receive data from the server
            recv_data = sock.recv(1024)
            print(("Received message from the server: " + bytes2str(recv_data)))

    except (KeyboardInterrupt, EOFError):
        sock.close()
        sys.exit(0)
