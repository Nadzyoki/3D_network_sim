from ursina import *

class Switch(Entity):
    def __init__(self, x=0,y=0,z=0,ip="127.0.0.1",port_con="5000",name="switch",ports=0):
        super().__init__(
            model="cube",
            collider='cube'
        )

        self.scale = (1,0.1,1)
        # self.collider = 'mesh'

        self.ip = ip
        self.port_con = port_con
        self.name = name
        self.x = x
        self.y = y
        self.z = z

        self.prt_lst = []

        self.Ports(ports)

    def Ports(self,num):
        z = -.45
        x = .5
        a=0
        for i in range(num):
            y = .25
            for j in range(2):
                port = PRT_fs(num=i+j+a, nm="FastEthernet", parent=self)
                port.x =x
                port.y=y
                port.z=z
                self.prt_lst.append(port)
                y+=-.5
            z+=.05
            a+=1

    def Replace(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

class PRT_fs(Entity):
    def __init__(self,num,nm,parent):
        super().__init__(
            name = (nm+str(num)),
            model = "cube",
            parent=parent
            )
        self.scale = (0.03,0.3,0.03)
        self.collider = 'cube'
        self.color = color.yellow
        self.addres=nm
        self.prnt = parent
        self.active = False
        self.activable= True

    def Actived(self):
        self.active = not(self.active)
        if self.active:
            self.color = color.cyan
        else :
            self.color = color.yellow
        print(self.active)