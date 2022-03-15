import threading
from ursina import *
from client import Client
from ursa import Ursa


class Main:
    def __init__(self,address):
        self.client = Client(address)
        self.ursan = Ursina(
            title='ursina',
            fullscreen=False,
        )
        self.ursa = Ursa(self.client)

        self.client.n_m(self.ursa)

        self.task1 = threading.Thread(target=self.client.main)
        self.task1.start()

        self.ursan.run()

        self.task1.join()


if __name__ == "__main__":
    main = Main(("127.0.0.1", 1234))
