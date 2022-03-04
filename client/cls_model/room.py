from .class_.player import *
from .class_.switch_cls import Switch
from .class_.vpc_cls import VPC
from .class_.map import Map

#main body
class Room:
    def __init__(self):
        self.pool = []

    def Light(self):
        p_l = PointLight(parent=camera, color=color.white, position=(0, 10, -1, 5))
        am_l = AmbientLight(color=color.rgba(100, 100, 100, 0.1))

    def Add_(self,obj):
        self.pool.append(obj)

    def Start(self):
        self.player = Player()
        self.player.name = "IAM"

        self.room = load_blender_scene('room1', reload=True)
        for e in self.room.children:
            e.collider = 'mesh'
        self.Switch_my = Switch(y=2, z=2, ports=4)
        self.nVPC = VPC(y=2, z=-1)
        # light in room
        self.Light()
        # add all object to pool
        self.Add_(self.player)
        self.Add_(self.Switch_my)
        self.Add_(self.nVPC)
        # create map
        self.map = Map( gr=self.room.ground)
        self.map.y = 2
        self.map.z = 1
        self.map.x = 1
        self.Add_(self.map)
        self.map.Update_pool(self.pool)

if __name__ == '__main__':
    app = Room()
    app.run()



