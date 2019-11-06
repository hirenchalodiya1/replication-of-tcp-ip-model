import threading
from core.utils import log
from core.middleware.checks.crc import CRC
from core.middleware.str_byte_conversion import str2bytes, bytes2str, bits2str


# Function used at the receiver side to decode data
def apply_check_decoding(data):
    return CRC(data).decode()


# Variables for holding information about connections
connections = []
total_connections = 0


# Client class, new instance created for each connected client
# Each instance has the socket and address that is associated with items
# Along with an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, sock, address, id_, name, signal):
        threading.Thread.__init__(self)
        self.socket = sock
        self.address = address
        self.id = id_
        self.name = name
        self.signal = signal

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server and send it back to every
    # client aside from the client that has sent it
    # .decode is used to convert the byte data into a printable string
    def run(self):
        while self.signal:
            try:
                data = self.socket.recv(1024)
                if data == b'':
                    raise ConnectionResetError
            except ConnectionResetError:
                log("Client " + str(self.address) + " has disconnected")
                self.signal = False
                self.socket.close()
                connections.remove(self)
                break

            if data != "":
                recv_data = bytes2str(data)

                print(
                    "Client " + str(self.id) + ": " + "Decoded Data from the client (in bits) is " + recv_data)
                dec_data_bits = apply_check_decoding(recv_data)

                # If remainder is all zeros then no error occurred
                if dec_data_bits != "":
                    err_msg = "No error found."
                    print(
                        "Client " + str(self.id) + ": " + "Decoded Data from the client is " + bits2str(dec_data_bits))
                else:
                    err_msg = "Error in data."
                print("Client " + str(self.id) + ": " + err_msg)
                self.socket.sendall(str2bytes(err_msg))


def new_connections(sock):
    try:
        while True:
            c_sock, address = sock.accept()
            global total_connections
            connections.append(Client(c_sock, address, total_connections, "Name", True))
            connections[len(connections) - 1].start()
            log("New connection at ID " + str(connections[len(connections) - 1]))
            total_connections += 1
    except (KeyboardInterrupt, EOFError):
        pass
