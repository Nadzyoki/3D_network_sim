# import socket,threading
# from threading import Thread
#
# class Client:
#     def __init__(self,address):
#         self.socket = socket.socket(
#             socket.AF_INET,
#             socket.SOCK_STREAM,
#         )
#         self.address = address
#
#     def set_up(self):
#         self.socket.connect(self.address)
#         self.socket.setblocking(False)
#
#     def send_data(self):
#         while True:
#             data = input()
#             self.socket.sendall(data.encode('utf-8'))
#
#     def listen_data(self):
#         while True:
#             data = self.socket.recv(2048)
#             print(f"Server get {data.decode('utf-8')}")
#
#     def start(self):
#         task_listen = Thread(target=self.listen_data())
#         task_listen.start()
#         task_listen.join()
#         task_send = Thread(target=self.send_data())
#         task_send.start()
#         task_send.join()
#
#
# if __name__ == "__main__":
#     ADDRESS = ("127.0.0.1", 1234)
#     client = Client(ADDRESS)
#     client.set_up()
#     client.start()


import socket
from threading import Thread

class Client:
    def __init__(self,address):
        # SERVER = "127.0.0.1"
        # PORT = 1234
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(address)

        def task():
            while True:
                data =  client.recv(4096)
                # print("От сервера :" ,in_data.decode())
                self.selector(data.decode('utf-8'))
        def task2():
            while True:
                out_data = input()
                client.sendall(bytes(out_data,'UTF-8'))
                print("Отпаравлено :" + str(out_data))

        t1 = Thread(target=task2)
        t2 = Thread(target=task)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def selector(self,data):
        n_data = data.split()
        match n_data[0]:
            case 'IMS':
                print(data)

if __name__ == "__main__":
    ADDRESS = ("127.0.0.1", 1234)
    client = Client(ADDRESS)