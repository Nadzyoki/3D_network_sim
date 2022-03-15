import socket

class Client:
    def __init__(self, address):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(address)

    def n_m(self,n):
        self.main_branch = n
    def main(self):
        while self.main_branch.work:
            data = self.client.recv(4096)
            print("От сервера :" ,data.decode())
            self.main_branch.Selector(data.decode('utf-8'))

if __name__ == "__main__":
    ADDRESS = ("127.0.0.1", 1234)
    client = Client(ADDRESS)
