from ursina import *
import ursina.color
# line = Entity(model=Mesh(vertices=[Vec3(0, 0, 0), Vec3(0, .5, 0)], mode='line'),color=ursina.color.cyan)

lines = []

def add_(vert):
    lines.append(Entity(model=Mesh(vertices=vert, mode='line',thickness = 7),color=ursina.color.cyan))