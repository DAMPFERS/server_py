import socket
from threading import Thread
import threading

SERVER = '127.0.0.1'
PORT = 1984



client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Алоха 0_o", 'UTF-8'))

def task():
    while True:
        in_data = client.recv(4096)
        print("От сервера: ", in_data.decode(encoding="utf-8"))
        
def task2():
    while True:
        out_data = input()
        client.sendall(bytes(out_data,"utf-8"))
        print("Отправлено: " + str(out_data))
        
t1 = Thread(target=task2)
t2 = Thread(target=task)

t1.start()
t2.start()