from ursina import *

class Map(Entity):
    def __init__(self,pool,gr):
        super().__init__()
        #field of map
        self.map = Entity(
            model="cube",
            collider='cube',
            parent=self,
            name='map'
        )
        self.sc=0.08
        self.map.scale = (gr.scale.x*self.sc, gr.scale.y*self.sc, .005)
        #add all object on map
        self.pool=[]
        for i in pool:
            point =self.Point(parent_obj=i,par=self)
            self.pool.append(point)

    class Point(Entity):
        def __init__(self,parent_obj,par):
            super().__init__(
                model="cube",
                collider="cube",
                scale=(0.02,0.02,0.02),
                color=color.red,
                parent=par
            )
            self.par = parent_obj
            self.name= self.par.name
            self.sc = 0.04

        def update(self):
            self.x = self.par.x * self.sc
            self.y = self.par.z * self.sc