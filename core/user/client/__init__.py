import sys
import settings
from core.utils import log
from core.user.client.connection import create_connection
from core.utils.str_byte_conversion import str2bytes
from core.device.datalink.client import client_dll
from core.device.physical.client import client_physical


def run_client():
    host = settings.SERVER_HOST
    port = settings.SERVER_PORT
    sock = create_connection((host, port))

    # Send data to server
    try:
        while True:
            # Input data to send
            orig_data = input("Enter data you want to send: ")

            # Convert data to list of frames
            enc_frames = client_dll(orig_data)
            log("Frames to be send: ", 2, end="")
            log(enc_frames, 2)

            # Implement coding scheme to each frame
            coded_frames = client_physical(enc_frames)
            log("Encoded frames: ", 2, end="")
            log(coded_frames, 2)

            # Send number of frames
            # num_of_frames = str(len(enc_frames))
            # encode_num_of_frames = client_dll(num_of_frames)[0]
            # sock.sendall(str2bytes(encode_num_of_frames))

            # Send the frames
            for frame in coded_frames:
                sock.sendall(str2bytes(frame))

            # receive data from the server
            # recv_data = sock.recv(settings.PACKET_SIZE)
            # print(("Received message from the server: " + bytes2str(recv_data)))

    except (KeyboardInterrupt, EOFError):
        sock.close()
        print()
        sys.exit(0)
