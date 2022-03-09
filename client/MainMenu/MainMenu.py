from ursina import *



class MainMenu(Entity):
    def __init__(self,ch):
        super().__init__(
            enabled=False
        )
        self.change = ch

    def Start(self):
        self.title = Text(text=dedent("<scale:2><azure>Simulation of Network in 3D"),
                          position=window.top_left,
                          origin=Vec2(-.5, 2)
                          )
        self.nameServer = Text(text=("Server : "+self.change.client.server_name),
                               position=window.bottom,
                               )
        self.rooms = WindowPanel(
            title="Room list",
            content=(

            ),
            popup=False,
            enabled=False
        )

        def startM():
            self.rooms.enabled = not (self.rooms.enabled)

        self.settings = WindowPanel(
            title="Settings",
            content=(

            ),
            popup=False,
            enabled=False
        )

        def startS():
            self.settings.enabled = not (self.settings.enabled)

        button_dict = {
            'Start': Func(startM),
            'Setting': Func(startS),
            'Exit': application.quit,
        }
        self.bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)


        window.color = color._32


    def Stop(self):
        self.enabled = False
        self.visible = False


