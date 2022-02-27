from ursina import *


class VPC(Entity):
    def __init__(self, x=0,y=0,z=0,ip="127.0.0.1",port_con="5000",name="vpc",ID_node='0',ID_port='0'):
        super().__init__()

        self.ID=ID_node
        self.ip = ip
        self.port_con = port_con
        self.name = name
        self.x = x
        self.y = y
        self.z = z

        self.activable = False
        self.key=Keybord(parent=self,nm=name)
        self.key.y-=.2
        self.key.x += .2
        self.mon=Monitor(parent=self,nm=name)
        self.port=Port(parent=self,nm=name,ID_port=ID_port)
        self.port.y -= .2
        self.port.x += .2
        self.port.z += .25

    def Replace(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z


class Keybord(Entity):
    def __init__(self,parent,nm):
        super().__init__(
            model="cube",
            collider='cube',
            parent=parent,
            name = ("Keybord of "+nm)
        )
        self.activable = False
        self.scale = (.5,.1,.5)


class Port(Entity):
    def __init__(self,parent,nm,ID_port):
        super().__init__(
            model="cube",
            collider='cube',
            parent=parent,
            name=("Port Ethernet of " + nm)
        )
        self.scale = (.05, .05, .005)
        self.ID = ID_port
        self.color = color.yellow
        self.activable = True


class Monitor(Entity):
    def __init__(self, parent, nm):
        super().__init__(
            model="cube",
            collider='cube',
            parent=parent,
            name=("Monitor of " + nm)
        )
        self.scale = (.1, .5, .5)
        self.activable = False