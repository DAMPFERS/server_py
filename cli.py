import socket
from threading import Thread
import threading

SERVER = '127.0.0.1'
PORT = 1984

t = [1,0,1,0,0,-1,-1,1,1]
t = [2,0,0,1,0,-1,-1,1,1]
t = [3,0,0,0,1,-1,1,1,1]
t = [4,0,0,1,0,-1,-1,-1,-1]

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Алоха", 'UTF-8'))
