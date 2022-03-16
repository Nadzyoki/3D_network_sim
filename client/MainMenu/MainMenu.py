from ursina import *
from ursina.prefabs.conversation import Conversation


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
        self.nameServer = Text(text=("Server : "+self.change.server_name),position=window.left,origin=Vec2(-.6, 4))


        self.rooms = WindowPanel(
            title="Room list",
            content=(

            ),
            popup=False,
            enabled=False
        )

        def startM():
            self.rooms.enabled = not (self.rooms.enabled)

        # def updateSN():
        #     self.change.Sender(what='WSN')

        def reconectServer():
            if servIN.text and servPRT.text:
                self.change.main_branch.Reconnect((servIN.text,int(servPRT.text)))
            else:
                self.change.main_branch.Reconnect()

        def sendMyName():
            self.change.Sender(what='CMN',data=nameUSR.text)

        # updSN = Button(text='update name server',)
        # updSN.on_click = Func(updateSN)

        servIN = InputField(name='ip server')
        servPRT = InputField(name='port server')
        nameUSR = InputField(name='name',default=self.change.my_name)

        sendMN = Button(text='send my name', )
        sendMN.on_click = Func(sendMyName)

        self.recSR = Button(text='reconnect server', )
        self.recSR.on_click = Func(reconectServer)

        self.settings = WindowPanel(
            title="Settings",
            content=(
                Space(),
                # updSN,
                self.recSR,
                servIN,
                servPRT,
                Space(),
                sendMN,
                nameUSR,
            ),
            popup=False,
            enabled=False
        )

        def startS():
            self.settings.enabled = not (self.settings.enabled)

        button_dict = {
            'Start': Func(startM),
            'Setting': Func(startS),
            'Exit': Func(self.change.Stop),
        }

        self.bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)

        window.color = color._32

    def update(self):
        self.nameServer.text = ("Server : " + self.change.server_name)

    def Stop(self):
        self.enabled = False
        self.visible = False
