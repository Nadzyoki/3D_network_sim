from main_scr.player import *
from cls_model.switch_cls import Switch
from cls_model.vpc_cls import VPC
class Main(Ursina):
    def __init__(self):
        super().__init__()
        self.player = Player()

        self.room = load_blender_scene('room1', reload=True)
        for e in self.room.children:
            e.collider = 'mesh'
        self.Switch_my = Switch(y=2, z=2, ports=4)
        self.nVPC = VPC(y=2, z=-1)

        self.Light()
        self.map = Map(pr=self)
        self.map.y = 2
        self.map.z = 1
        self.map.x = 1
        # self.map.Chan(self.player.x, self.player.z)

    def Light(self):
        p_l = PointLight(parent=camera, color=color.white, position=(0, 10, -1, 5))
        am_l = AmbientLight(color=color.rgba(100, 100, 100, 0.1))

    # def update(self):
    #     self.map.Chan(self.player.x, self.player.z)
    #     print(self.player.x, self.player.z)



class Map(Entity):
    def __init__(self,pr):
        super().__init__(
            parent=pr
        )
        self.parent=pr

        self.map = Entity(
            model="cube",
            collider='cube',
            parent=self,
            name='map'
        )
        self.map.scale = (1.2, 1.2, .005)

        self.point = Entity(
            model="cube",
            collider="cube",
            parent=self,
            name=(f"point {self.parent.player.x} {self.parent.player.y} ")
        )
        self.point.scale=(0.02,0.02,0.02)
        self.point.color=color.red

    def update(self):
        self.Chan(self.parent.player.x, self.parent.player.z)
        self.point.name=(f"point {self.parent.player.x.toFixed(2)} {self.parent.player.z.toFixed(2)} ")

    def Chan(self,x,y):
        sc = 0.04
        self.point.x = x*sc
        self.point.y = y * sc



if __name__ == '__main__':
    # window.vsync = False

    app = Main()
    app.run()



