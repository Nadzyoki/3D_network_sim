from cls_model.player import *
from cls_model.switch_cls import Switch
from cls_model.vpc_cls import VPC
from cls_model.map import Map

#network
from ursinanetworking import *

#end network

#main body
class Main(Ursina):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.player.name = "IAM"

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







if __name__ == '__main__':
    # window.vsync = False

    app = Main()
    app.run()



