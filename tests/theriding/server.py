import socket
import threading
#
#
# class Server:
#     def __init__(self, address):
#         self.socket = socket.socket(
#             socket.AF_INET,
#             socket.SOCK_STREAM,
#         )
#         self.address = address
#         self.server_name = "main server"
#
#     def set_up(self):
#         self.socket.bind(self.address)
#         self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         self.socket.listen(5)
#         self.socket.settimeout(0)
#         self.socket.setblocking(False)
#
#     def selector(self, data, user):
#         n_data = data.decode('utf-8').split()
#
#         match n_data[0]:
#             case 'CMN':
#                 user.name = n_data[1]
#                 return None
#             case 'WMN':
#                 return user.name
#             case 'WSN':
#                 return self.server_name
#
#     def start(self):
#         while True:
#             user_socket, address = self.socket.accept()
#             newthread = self.ClientThread(address, user_socket, self)
#             newthread.start()
#
#
#     class ClientThread(threading.Thread):
#         def __init__(self, clientaddress, clientsocket, main,):
#             threading.Thread.__init__(self)
#             self.server = main
#             self.csocket = clientsocket
#             self.name = "No name"
#             print(f"New connect {clientaddress}")
#
#         def run(self):
#             while True:
#                 data = self.csocket.recv(2048)
#                 d_data = data.decode('utf-8')
#                 if d_data == '':
#                     continue
#                 else:
#                     ans = self.server.selector(data, self)
#                     if ans:
#                         self.csocket.sendall(ans.encode('utf-8'))
#                     else:
#                         continue
#
#
# if __name__ == "__main__":
#     ADDRESS = ("127.0.0.1", 12343)
#     server = Server(ADDRESS)
#     server.set_up()
#     server.start()

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket,main):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.server = main
        self.name = "Noname"
        print("Новое подключение: ", clientAddress)

    def run(self):
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode('utf-8')
            print(msg)

            if msg == '':
                print("Отключение")
                break
            else:
                ans = self.server.selector(msg,self)
                if ans:
                    self.csocket.sendall(ans.encode('utf-8'))
                    print(f'send {ans}')


class Server:
    def __init__(self,address):
        # LOCALHOST = "127.0.0.1"
        # PORT = 1234

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server.bind(address)
        print("Сервер запущен!")
        self.server_name = "Main server"


        while True:
            server.listen(1)
            clientsock, clientAddress = server.accept()
            newthread = ClientThread(clientAddress, clientsock,self)
            newthread.start()

    def selector(self, data, user):
        n_data = data.split()

        match n_data[0]:
            case 'CMN':
                user.name = n_data[1]
                return ('IMS '+'succes change name')
            case 'WMN':
                return ('IMS '+'your name '+user.name)
            case 'WSN':
                return ('SN '+self.server_name)

        return None

if __name__ == "__main__":
    ADDRESS = ("127.0.0.1", 1234)
    server = Server(ADDRESS)
