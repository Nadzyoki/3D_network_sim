from ursina import *


class MAINMENU(Entity):
    def __init__(self,ch):
        super().__init__(
            enabled=False
        )
        self.change = ch
        self.pool = []

    def Start(self) -> None:
        #start class
        # self.enabled = True

        # input fields
        self.servIN = InputField(name='ip server')
        self.servPRT = InputField(name='port server')
        self.nameUSR = InputField(name='name')

        #titels
        self.name_project = Text(text=dedent("<scale:2><azure>Simulation of Network_ in 3D"),
                          position=window.top_left,
                          origin=Vec2(-.5, 2)
                          )
        self.pool.append(self.name_project)
        self.name_server = Text(text=("Server : " + self.change.server_name),
                                position=window.left,
                                origin=Vec2(-.6, 4)
                                )
        self.pool.append(self.name_server)

        #function for start panel
        def enableFunc(panel):
            panel.enabled = not (panel.enabled)

        #buttons
        self.sendMN = Button(text='send my name', )
        self.recSR = Button(text='reconnect server', )

        #function for on_click
        def reconectServer():
            if self.servIN.text and self.servPRT.text:
                self.change.main_branch.Reconnect((self.servIN.text,int(self.servPRT.text)))
            else:
                self.change.main_branch.Reconnect()

        def sendMyName():
            self.change.Sender(what='CMN',data=self.nameUSR.text)

        #on_click function
        self.sendMN.on_click = Func(sendMyName)
        self.recSR.on_click = Func(reconectServer)

        #panels
        self.start_room = WindowPanel(
            title="Room list",
            content=(

            ),
            popup=False,
            enabled=False
        )
        self.pool.append(self.start_room)
        self.settings = WindowPanel(
            title="Settings",
            content=(
                Space(),
                # updSN,
                self.recSR,
                self.servIN,
                self.servPRT,
                Space(),
                self.sendMN,
                self.nameUSR,
            ),
            popup=False,
            enabled=False
        )
        self.pool.append(self.settings)

        #left panel with buttons
        button_dict = {
            'Start': Func(enableFunc,self.start_room),
            'Setting': Func(enableFunc,self.settings),
            'Exit': Func(self.change.Stop),
        }
        self.bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)
        self.pool.append(self.bl)

        #init of background
        window.color = color._32

    def update(self):
        self.name_server.text = ("Server : " + self.change.server_name)

    def Stop(self):
        for i in self.pool:
            destroy(i,delay=0)
        self.enabled = False
        self.visible = False
