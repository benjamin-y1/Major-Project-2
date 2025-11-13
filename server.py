import socket
from _thread import *
from player import Board, Cell
import pickle

server = "192.168.68.60"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.bind((server, port))

except socket.error as e:

    print("This went wrong")

s.listen(2)

print("Waiting for a connection, Server Started")

boards = [Board(2, 10, 10), Board(2, 600, 10)]
for i in boards:
    i.initiate()

def threaded_client(conn, player):
    conn.send(pickle.dumps(boards[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            boards[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = boards[(player + 1) % 2]

            print("Received: ", data)
            print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost Connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
