import socket
from objects import Snake
import random
from _thread import *
import pickle

server = "192.168.1.10"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server open")

players = {}
food = (random.randint(1, 24), random.randint(1, 24))


def threaded_client(conn, addr):
    global food, players
    players[addr] = Snake(5, 6, 20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    conn.send(pickle.dumps((players[addr], addr)))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[addr] = data

            if not data:
                print("Disconnecting")
                break
            else:
                for i in players:
                    if players[i].bodies[0][0] == food[0] and players[i].bodies[0][1] == food[1]:
                        players[i].eat()
                        food = (random.randint(1, 24), random.randint(1, 24))
                for q in players:
                    if players[q] != players[addr]:
                        if players[addr].bodies[0] in players[q].bodies:
                            quit()

            conn.sendall(pickle.dumps((players, food)))

        except:
            break

    players.pop(addr)
    conn.close()


while True:
    conn, addr = s.accept()
    print(f"{addr} connected to the server")
    start_new_thread(threaded_client, (conn, addr))
