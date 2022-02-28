
class State_machine:
    def __init__(self,states):
        self.list_state = states
        self.now = self.list_state[0]

    def ChangeState(self,ste):
        if ((ste in self.list_state) and not(ste == self.now)) : self.now = ste

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
