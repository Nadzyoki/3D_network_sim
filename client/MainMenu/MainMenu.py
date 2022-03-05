from ursina import *


class MainMenu:
    def __init__(self,ch):
        self.change = ch
        self.pool_main_menu = []

    def Start(self):
        self.title = Text(text=dedent("<scale:2><azure>Simulation of Network in 3D"),
                          position=window.top_left,
                          origin=Vec2(-.5, 2)
                          )
        button_dict = {
            'Start': Func(self.change.Change,'IR'),
            'Setting': Func(self.change.Change,'SM'),
            'Exit': application.quit,
        }
        self.bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)
        window.color = color._32
        self.pool_main_menu.append(self.title)
        self.pool_main_menu.append(self.bl)

    def Stop(self):
        for i in self.pool_main_menu:
            i.enabled = False
        self.pool_main_menu.clear()

