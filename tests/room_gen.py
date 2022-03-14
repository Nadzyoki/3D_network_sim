from ursina import *


class GenRoom:
    def __init__(self,map_):
        self.map=map_
        for i in range(1,2):
            Entity(model=Plane(vertices=(self.map[i],self.map[i+1],self.map[i+2],self.map[i+3],)), color=color.cyan)




if __name__ == '__main__':
    app =Ursina()
    EditorCamera()
    map = [
        Vec3(0,0,0),
        Vec3(5,0,0),
        # (5, 0, 0),
        Vec3(5, 5, 0),
        # (5, 5, 0),
        Vec3(0, 5, 0),
        # (0, 5, 0),
        # (0, 0, 0),
    ]
    # front =  Entity(model=Plane(vertices=map), texture='brick', rotation_x=-90)
    # Entity(model='cube', color=color.green, scale=.05)
    # GenRoom(map)
    e = Entity(model=Terrain('pixil-frame-0', skip=1), scale=(10,1,10))
    # Entity(model='plane', scale=e.scale, color=color.red)
    app.run()