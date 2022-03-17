from ursina.prefabs.trail_renderer import TrailRenderer

from .class_.player import *


class ROOM(Entity):
    def __init__(self,ch=None,room=None,server = None):
        super().__init__(
            enabled=False
        )
        self.change = ch
        self.pool_obj = server
        self.room = room
        self.pool = []

    def Start(self) -> None:
        self.enabled = True

        # self.room = load_blender_scene('room1', load=False,reload=True,)
        self.room = Entity(model='cube',scale=(30,.1,30),color=color.green)
        # trail_renderer = TrailRenderer(parent=self.room)
        self.pool.append(self.room)
        # for e in self.room.children:
        #     e.collider = 'mesh'

        self.player = Player(scn=self, name="IAM",)
        self.pool.append(self.player)
        self.am_l = AmbientLight(color=color.rgba(100, 100, 100, 0.2))
        self.pool.append(self.am_l)


    def Stop(self):
        for i in self.pool:
            destroy(i,delay=0)
        self.enabled = False
        self.visible = False
        mouse.locked = False

    def input(self, key):
        if key == 'space':
            self.change.Change('MM')

if __name__ == '__main__':
    app = Room()
    app.run()



