import socket
import pickle

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.68.60"
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
            board = pickle.loads(self.client.recv(16384))
            return board

        except:
            print("connection failed")

    def send_board(self, board):
        try:
            self.client.sendall(pickle.dumps(board))
        except:
            print("Couldn't Send Board")

    def receive_board(self):
        try:
            return pickle.loads(self.client.recv(16384))
        except:
            print("Couldn't receive board")