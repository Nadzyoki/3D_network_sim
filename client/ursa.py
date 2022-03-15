from ursina import *
from In_Room.Room import Room
from MainMenu.MainMenu import MainMenu


class Ursa(Entity):
    def __init__(self,client):
        self.client = client
        self.my_name = 'No name'
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


    def Selector(self,data):
        n_data = data.split()
        print("some in selector")
        match n_data[0]:
            case 'IMS':
                print(data)
            case 'SN':
                self.server_name=n_data[1]
            case 'MN':
                self.my_name = n_data[1]

    def Sender(self,what,data):
        send = lambda x: self.client.sendall(x.encode('utf-8'))
        match what:
            case 'WSN':
                send('WSN')
            case 'WMN':
                send('WMN')
            case 'CMN':
                send('CMN '+data)
