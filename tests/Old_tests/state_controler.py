####################################################################
# Work with statement
####################################################################
def Statement(self, ev):
    if (self.now_state + ev) in self.map_event:
        return self.map_event[self.now_state + ev]


def Chage_statement(self, ev):
    if not (ev == None):
        self.now_state = ev
        self.gui.Disable_menu(ev)
        self.on_move()
