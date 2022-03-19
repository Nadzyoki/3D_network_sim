import threading
from ursina import *
from Network_.CLIENT import CLIENT
from Window_.URSA import URSA
from Window_.Splash_ import Splash_my


class MAIN:
    def __init__(self,address):
        self.address =address

        self.client = CLIENT()
        self.main_ursina = Ursina(
            title='ursina',
            fullscreen=False,
            borderless = False ,
            show_ursina_splash = False,
        )
        Splash_my.Logo()
        self.window = URSA(self, self.client)
        self.client.SetMainWindow(self, self.window)
        self.Reconnect()
        self.main_ursina.run()


    def Reconnect(self,address=None):
        if self.client.may_work:
            self.window.Sender('IDS')
            self.client.may_work = False

        if not address:
            self.client.Connect(self.address)
        else:
            self.client.Connect(address)
        self.task1 = threading.Thread(target=self.client.Main)
        self.task1.start()


    def Stop(self):
        print('goodbye')
        application.quit()


if __name__ == "__main__":
    main = MAIN(("127.0.0.1", 6060))
