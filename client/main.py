from ursina import *
from In_Room.Room import Room
from MainMenu.MainMenu import MainMenu
from Network.client import Client


class Main(Ursina):
    def __init__(self,client):
        self.server_name = client.server_name

        super().__init__(
            title='ursina',
            fullscreen=True,
        )

        self.scence = 'MM'

        self.MM = MainMenu(self)
        # self.IR = Room()

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


if __name__ == "__main__":
    ADDRESS = ("127.0.0.1", 1234)
    client = Client(ADDRESS)
    main = Main(client)
    client.set_up()
    client.start(main)
