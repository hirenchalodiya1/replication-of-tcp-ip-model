import threading
from core.utils import log
from core.utils.str_byte_conversion import str2bytes, bytes2str
from core.device.datalink.server import server_dll

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
        self.frames = ""
        self.num_of_frames = 0
        self.error = False
        self.socket.settimeout(0.1)

    def __str__(self):
        return str(self.id) + " " + str(self.address)

    # Attempt to get data from client
    # If unable to, assume client has disconnected and remove him from server data
    # If able to and we get data back, print it in the server
    def run(self):
        while self.signal:
            try:
                if self.socket.sendall(b'11111111') == 0:
                    raise ConnectionResetError
                while True:
                    try:
                        chunk = self.socket.recv(2048)
                    except OSError:
                        break
                    frame = bytes2str(chunk)
                    self.frames += str(frame)
                if self.frames == "":
                    continue
                err_msg = self.check_data()
                self.display(err_msg)
                self.return_data(err_msg)
            except (ConnectionResetError, BrokenPipeError):
                log("Client " + str(self.address) + " has disconnected")
                self.signal = False
                self.socket.close()
                connections.remove(self)
                break

            # if frame != "":
            # if self.error:
            #     if self.num_of_frames > 0:
            #         self.num_of_frames -= 1
            #     else:
            #         self.error = False
            # else:
            # if self.num_of_frames == 0:
            #     self.set_len_rec_frames(frame)
            # else:
            #     if len(self.frames) < self.num_of_frames:
            #         dec_frame = bytes2str(frame)
            #         self.frames.append(str(dec_frame))

            # Check data if all the frames are received
            # if self.num_of_frames != 0 and len(self.frames) == self.num_of_frames:
            #     err_msg = self.check_data()
            #     self.display(err_msg)
            #     self.return_data(err_msg)

    def set_len_rec_frames(self, frame):
        num_frames_bits = [bytes2str(frame)]
        num_frames = server_dll(num_frames_bits)
        self.num_of_frames = int(num_frames)

    def check_data(self):
        log("Client %s: '%s' bits received" % (str(self.id), self.frames), 2)
        dec_data = server_dll(self.frames)

        if dec_data != "":
            err_msg = "No error found."
            self.display("Decoded data from client: " + dec_data)
        else:
            err_msg = "Error in data."
        self.reset_data()
        return err_msg

    def return_data(self, data):
        self.socket.sendall(str2bytes(data))

    def reset_data(self):
        self.frames = ""
        self.num_of_frames = 0

    def display(self, msg):
        log("Client " + str(self.id) + ": " + msg)


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
