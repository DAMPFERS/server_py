import socket, threading 

HOST_IP = "127.0.0.1"   # IP-адрес хоста (localhost)
PORT = 1984             # Порт, на котором будет работать сервер

class ClientThread(threading.Thread): # Определение класса ClientThread, наследующего от threading.Thread

    def __init__(self, client_Addres, client_socket): 
        threading.Thread.__init__(self) # Инициализация потока
        self.csocket = client_socket # Сохранение сокета клиента
        print("Новое подключение", client_Addres) # Вывод сообщения о новом подключении

    def run(self): # Метод, который будет выполняться в новом потоке
        msg = '' # Инициализация пустой строки для сообщения
        while True:                             # Бесконечный цикл для обработки сообщений от клиента
            data = self.csocket.recv(4096)      # Получение данных от клиента (чанк до 4096 байт)
            msg = data.decode()                 # Декодирование полученных данных в строку
            print(msg)                          # Вывод полученного сообщения
            if msg == '':                       # Проверка, пустое ли сообщение (клиент отключился)
                print("Отключение :(")          # Вывод сообщения об отключении
                break                           # Выход из цикла
            elif msg == "Какая-то команда от клиента":                              # Проверка, соответствует ли сообщение определенной команде
                self.csocket.send(bytes("Ответ сервера клиенту", encoding="utf-8")) # Отправка ответа клиенту




def main(): # Основная функция
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # Создание сокета сервера
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        # Настройка сокета для повторного использования адреса

    server.bind((HOST_IP, PORT))                                        # Привязка сокета к указанному IP-адресу и порту
    print("Сервер восстал!!!")                                          # Вывод сообщения о запуске сервера

    while True:                                                         # Бесконечный цикл для приема новых подключений
        server.listen(4)                                                # Прослушивание входящих подключений (максимум зависит от параметра, сейчас максимум 4 в очереди)
        client_sock, client_Addres = server.accept()                    # Принятие нового подключения
        new_thread = ClientThread(client_Addres, client_sock)           # Создание нового потока для обработки клиента
        new_thread.start()                                              # Запуск нового потока





if __name__ == "__main__":  # Проверка, запущен ли скрипт напрямую
    main()                  # Вызов основной функции