
import socket, threading
LOCALHOST = '127.0.0.1'
PORT = 1984


def start_server_one():
    
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((LOCALHOST, PORT))
        print("ОН ВОССТАЛ !!!")
        server.listen(4)
        while(True):
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            a = input(' Отправляем? ')
           # content = load_page_from_get_request('Hello')
            content = "HI".encode('utf-8')
            client_socket.send(a)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Finish')
#def load_page_from_get_request(request_data):
 #   HDRS = 'HTTP/1.1 200 OK\r\nContent_Type: text/html; charset=utf-8\r\n\r\n'
 #   return HDRS.encode('utf-8') + request_data.encode('utf-8')





if __name__ == '__main__':
    start_server_one()
