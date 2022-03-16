import threading
from ursina import *
from client import Client
from ursa import Ursa


class Main:
    def __init__(self,address):
        self.address =address

        self.client = Client(self.address)
        self.main_ursina = Ursina(
            title='ursina',
            fullscreen=False,
        )
        self.window = Ursa(self,self.client)

        self.client.n_m(self, self.window)

        self.task1 = threading.Thread(target=self.client.main)
        self.task1.start()

        self.main_ursina.run()



    def Reconnect(self,address=None):
        if self.client.may_work:
            self.window.Sender('IDS')
            self.client.may_work = False

        if not address:
            self.client.Connect(self.address)
        else:
            self.client.Connect(address)
        self.task1 = threading.Thread(target=self.client.main)
        self.task1.start()


    def Stop(self):
        print('goodbye')
        application.quit()


if __name__ == "__main__":
    main = Main(("127.0.0.1", 1234))
