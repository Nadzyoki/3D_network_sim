import threading
from ursina import *
from In_Room.Room import Room
from MainMenu.MainMenu import MainMenu
from Network.client import Client


class Ursa(Entity):
    def __init__(self,client):
        self.client = client
        self.server_name = "no"
        self.work = True

        super().__init__()

        self.scence = 'MM'

        self.MM = MainMenu(self)

        self.scence_all = [
            self.MM,
            # self.IR,
        ]
        self.scence_dic = {
            'MM': self.MM,
            # 'IR': self.IR,
        }
        self.scence_hope = {
            # 'MMIR': 'IR',
            'MMMM': 'MM',

            'IRMM': 'MM',
        }
        self.Change('MM')

    def Ver(self, to):
        if (self.scence + to) in self.scence_hope:
            return self.scence_hope[self.scence + to]

    def Change(self, to):
        if not (self.Ver(to) == None):
            for i in self.scence_all:
                i.Stop()

            self.scence = self.Ver(to)
            self.scence_dic[self.scence].Start()

    def StartRoom(self, id):
        self.IR = Room(ch=self, room=self.server.Room(id),
                       server=self.server)
        self.Change('IR')

    def StopRoom(self):
        self.IR = None
        self.Change('MM')

    def selector(self,data):
        n_data = data.split()
        print("some in selector")
        match n_data[0]:
            case 'IMS':
                print(data)
            case 'SN':
                self.server_name=n_data[1]

    def qu(self):
        self.work = False
        application.quit()


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


