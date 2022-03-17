from ursina import *
from In_Room.Room import Room
from MainMenu.MainMenu import MainMenu


class Ursa(Entity):
    def __init__(self,main,client=None):
        self.main_branch = main
        self.client = client
        self.my_name = 'No name'
        self.server_name = "no"

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
        if data:
            n_data = data.split()
            match n_data[0]:
                case 'IMS':
                    print(data)
                case 'SN':
                    self.server_name=n_data[1]
                case 'MN':
                    self.my_name = n_data[1]
        elif data == '':
            self.server_name="no"
            self.main_branch.Reconnect()

    def Sender(self,what,data=None):
        if self.client.may_work:
            send = lambda x: self.client.client.sendall(x.encode('utf-8'))
            match what:
                case 'WSN':
                    send('WSN')
                case 'WMN':
                    send('WMN')
                case 'CMN':
                    if not(data==None):
                        send('CMN '+data)
                case 'IDS':
                    send('IDS')

    def Stop(self):
        if self.client.may_work:
            self.Sender('IDS')
            self.client.ON = False
            self.client.may_work =False
        else:
            self.End()

    def End(self):
        self.main_branch.Stop()
