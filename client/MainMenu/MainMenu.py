from ursina import *



class MainMenu(Entity):
    def __init__(self,ch):
        super().__init__(
            enabled=False
        )
        self.change = ch

    def Start(self):
        self.enabled = True
        self.title = Text(text=dedent("<scale:2><azure>Simulation of Network in 3D"),
                          position=window.top_left,
                          origin=Vec2(-.5, 2)
                          )
        self.nameServer = Text(text=("Server : "+self.change.server_name),)
        self.rooms = WindowPanel(
            title="Room list",
            content=(

            ),
            popup=False,
            enabled=False
        )

        def startM():
            self.rooms.enabled = not (self.rooms.enabled)

        def updateSN():
            self.change.client.client.sendall('WSN'.encode('utf-8'))

        updSN = Button(text='update name server',)
        updSN.on_click = Func(updateSN)

        self.settings = WindowPanel(
            title="Settings",
            content=(
                updSN,
            ),
            popup=False,
            enabled=False
        )

        def startS():
            self.settings.enabled = not (self.settings.enabled)

        button_dict = {
            'Start': Func(startM),
            'Setting': Func(startS),
            'Exit': Func(application.quit),
        }

        self.bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)

        window.color = color._32

    def update(self):
        self.nameServer.text = ("Server : " + self.change.server_name)

    def Stop(self):
        self.enabled = False
        self.visible = False
