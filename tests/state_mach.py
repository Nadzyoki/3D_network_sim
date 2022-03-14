
class Old_State_machine:
    def __init__(self,states):
        self.list_state = states
        self.now = self.list_state[0]

    def ChangeState(self,ste):
        if ((ste in self.list_state) and not(ste == self.now)) :
            self.now = ste
        else :
            self.now = self.list_state[0]

    def NextState(self):
        if (self.list_state.index(self.now) == (len(self.list_state)-1)):
            self.now = self.list_state[0]
        else :
            self.now = self.list_state[self.list_state.index(self.now)+1]

    def PastState(self):
        if (self.list_state.index(self.now) == 0):
            self.now = self.list_state[len(self.list_state) - 1]
        else:
            self.now = self.list_state[self.list_state.index(self.now) - 1]

    def NowState(self):
        return self.now


class State_machine:
    def __init__(self, m_e, first):
        self.m_e = m_e
        self.now = first

    def Event(self, ev):
        if (self.now + ev) in self.m_e:
            self.now = self.m_e[self.now + ev]


map_event = {

    'MoveEsc': 'Esc',
    'MoveTab': 'Tab',

    'TabTab': 'Move',

    'EscEsc': 'Move',
}


class Connection_tool:
    def __init__(self, mach):
        self.One = None
        self.Two = None
        self.Machine = mach

    def Connect(self, address):
        if self.One == None:
            self.One = address
        elif self.Two == None:
            self.Two = address
            self.Send()
        else:
            pass

    def Send(self):
        self.Machine.connect_ports(self.One, self.Two)
        self.One = None
        self.Two = None
