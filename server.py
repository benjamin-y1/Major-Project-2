import socket
from _thread import *
from player import Board, Cell
import pickle
import random, os, puz

crosswords = "C:\\Users\\yangb\\Downloads\\2025 mondays"
a = random.choice(os.listdir(crosswords))
crossword_path = os.path.join(crosswords, a)

p = puz.read(crossword_path)
numbering = p.clue_numbering()

grid = puz.Grid(p.fill, p.width, p.height)

grid_access = []

for row in range(p.height):
    grid_access.append(''.join(grid.get_row(row)))

numbering = p.clue_numbering()

grid_numbers = [[0 for x in range(p.width)] for y in range(p.height)]

for clue in numbering.across:
    if clue['num']:
        grid_numbers[clue['row']][clue['col']] = clue['num']

for clue in numbering.down:
    if clue['num']:
        grid_numbers[clue['row']][clue['col']] = clue['num']

print(grid_access)

server = "192.168.68.60"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.bind((server, port))

except socket.error as e:

    print("This went wrong")

s.listen(2)

print("Waiting for a connection, Server Started")

boards = [Board(15, 15,10, 10, grid_access, grid_numbers), Board(15, 15, 1000, 10, grid_access, grid_numbers)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(boards[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(16384))
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
