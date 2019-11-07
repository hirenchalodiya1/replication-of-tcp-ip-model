from core.user.client.connection import create_connection
from core.utils.str_byte_conversion import str2bytes
import sys
from core.device.datalink.client import client_dll


def run_client():
    host = 'localhost'
    port = 6784
    sock = create_connection((host, port))

    # Send data to server
    try:
        while True:
            # Input data to send
            orig_data = input("Enter data you want to send: ")

            # Convert data to list of frames
            enc_frames = client_dll(orig_data)
            print(enc_frames)

            # Send number of frames
            # num_of_frames = str(len(enc_frames))
            # encode_num_of_frames = client_dll(num_of_frames)[0]
            # sock.sendall(str2bytes(encode_num_of_frames))

            # Send the frames
            for frame in enc_frames:
                sock.sendall(str2bytes(frame))

            # receive data from the server
            # recv_data = sock.recv(settings.PACKET_SIZE)
            # print(("Received message from the server: " + bytes2str(recv_data)))

    except (KeyboardInterrupt, EOFError):
        sock.close()
        sys.exit(0)
