import socket

class Client:
    def __init__(self, address):
        self.may_work = False
        self.ON = True
        self.Connect(address)

    def Connect(self,address):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(address)
            self.may_work = True
            print('Успешно подключился к серверу')
            self.client.sendall('WSN'.encode('utf-8'))
        except ConnectionRefusedError:
            print('Нет сервера для подключения')



    def n_m(self,main,window):
        self.main_branch = main
        self.window = window

    def main(self):
        while self.may_work:
            data = self.client.recv(4096)
            print("От сервера :" ,data.decode())

            if data.decode('utf-8') == "Goodbye":
                self.may_work=False
                break
            if data.decode('utf-8') == "":
                self.may_work = False
                break
            self.window.Selector(data.decode('utf-8'))
        if not self.ON:
            self.window.End()

if __name__ == "__main__":
    ADDRESS = ("127.0.0.1", 1234)
    client = Client(ADDRESS)
