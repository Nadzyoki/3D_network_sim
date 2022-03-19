from ursina import *
import Splash
from Client import Client


class Main:
    def __init__(self):
        self.app = Ursina()
        self.client = Client()
        #splash
        Splash.Logo('Hello')
        self.Connect()

        self.app.run()

    def Connect(self,start_=None):
        # registration
        # input
        addrSRV = InputField(name='ip server')
        portSRV = InputField(name='port server')
        nameUSR = InputField(name='name')
        passwUSR = InputField(name='password')
        inp_list = []
        inp_list.append(addrSRV)
        inp_list.append(portSRV)
        inp_list.append(nameUSR)
        inp_list.append(passwUSR)
        # button
        sendMN = Button(text='connect', )

        def fer_data():
            for i in inp_list:
                if not (i.text):
                    tip = Tooltip('<black>Fill all', enabled=True, background_color=rgb(243, 243, 55))
                    destroy(tip, delay=3)
                    return False
            return True

        def TryConnect():
            if fer_data():
                if self.client.connect(addrSRV.text, int(portSRV.text), nameUSR.text, passwUSR.text):
                    tip = Tooltip('<black>Server connect', enabled=True, background_color=rgb(97, 220, 66))
                    destroy(tip, delay=6)
                    destroy(wp_registration, delay=6)
                else:
                    tip = Tooltip('<black>Server dont connect', enabled=True, background_color=rgb(165, 32, 32))
                    destroy(tip, delay=6)

        # panel of registartion
        sendMN.on_click = Func(TryConnect)
        wp_registration = WindowPanel(
            title='Registration',
            content=(
                Space(),
                Text(text='Address server'),
                addrSRV,
                Text(text='Port server'),
                portSRV,
                Text(text='Name user'),
                nameUSR,
                Text(text='Password user'),
                passwUSR,
                sendMN,
            ),
            popup=False,
        )


if __name__ == "__main__":
    main = Main()