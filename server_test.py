import socket, threading

#192.168.0.1
#server = socket.socket(socket.AF_INET, socket.SOCK_STERAM)
#server.bind(('127.0.0.1', 1984)) почему-то на работает 

#def start_my_server():
#    server = socket.create_server(('127.0.0.1', 1984))
#    server.listen(4)
#    print("ОН ВОССТАЛ !!!")
#    client_socket, address = server.accept()
#    data = client_socket.recv(1024).decode('utf-8')
#    print(data)
#    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
#    content = 'Accept my boy.......'.encode('utf-8')
#    client_socket.send(HDRS.encode('utf-8') + content)
 #   print('What(o_0)?')

#start_my_server()

LOCALHOST = '127.0.0.1'
PORT = 1984

server = socket.create_server((LOCALHOST, PORT))
print("ОН ВОССТАЛ !!!")



class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Новое подключение: ", clientAddress)
    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == '':
                print("Ушёл")
                break



    
while True:
    server.listen(2)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress,clientsock)
    newthread.start()
