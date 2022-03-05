from ursina import *
from In_Room.Room import Room
from MainMenu.MainMenu import MainMenu
from SettingMenu.SettingMenu import SettingMenu

class Main(Ursina):
    def __init__(self):
        super().__init__(
            title='ursina'
        )

        self.scence='MM'

        # self.scence_change={
        #     'MM': self.Change('MM'), #Main Menu
        #     'SM': self.Change('SM'), #Setting Menu
        #     'IR': self.Change('IR'), #In Room
        # }

        self.MM = MainMenu(self)
        self.SM = SettingMenu(self)
        self.IR = Room(self)


        self.scence_all=[
            self.MM,
            self.SM,
            self.IR,
        ]
        self.scence_dic = {
            'MM':self.MM,
            'SM':self.SM,
            'IR':self.IR,
        }
        self.scence_hope={
            'MMIR' : 'IR',
            'MMSM' : 'SM',
            'MMMM' : 'MM',
        }
        self.Change('MM')

    def Ver(self,to):
        if (self.scence+to) in self.scence_hope:
            return self.scence_hope[self.scence+to]

    def Change(self,to):
        if not(self.Ver(to) == None):
            for i in self.scence_all:
                i.Stop()
            self.scence = self.Ver(to)
            self.scence_dic[self.scence].Start()


if __name__ == "__main__":
    main =Main()
    main.run()