from ursina import *

class GUI(Entity):
    def __init__(self):
        super.__init__()
        self.now_state = 'MM'
        self.main_event = {

            'MMPG': 'PG',

            'SPMM': 'MM',
            'SPPG':'PG',

            'PGSP': 'SP',

        }

    def update(self):
        match self.now_state:
            case 'MM':
                pass


    def Statement(self, ev):
        if (self.now_state + ev) in self.map_event:
            return self.map_event[self.now_state + ev]
        else :
            return None

    def Chage_statement(self,ev):
        if not(ev == None):
            self.now_state=ev

    def input(self, key):
        match self.now_state:
            case 'PG':
                if (key == 'escape'):
                    self.Chage_statement(self.Statement('SP'))