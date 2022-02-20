from ursina import *

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
        self.point.name=(f"{self.parent.player.name}")

    def Chan(self,x,y):
        sc = 0.04
        self.point.x = x*sc
        self.point.y = y * sc