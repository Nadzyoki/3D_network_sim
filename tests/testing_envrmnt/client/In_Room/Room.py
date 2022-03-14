from .class_.player import *
from ursina.ursinastuff import _destroy
from .class_.switch_cls import Switch
from .class_.vpc_cls import VPC
from .class_.map import Map

class Room(Entity):
    def __init__(self,ch=None,room=None,server = None):
        super().__init__(
            enabled=False
        )
        self.room = room
        self.room = load_blender_scene('room1', reload=False)
        for e in self.room.children:
            e.collider = 'mesh'
        self.change = ch
        self.pool = server
        self.player = Player(ch=self.change,name = "IAM")
        self.am_l = AmbientLight(color=color.rgba(100, 100, 100, 0.2))

    def Start(self):
        pass

    def Stop(self):

        mouse.locked = False

if __name__ == '__main__':
    app = Room()
    app.run()



