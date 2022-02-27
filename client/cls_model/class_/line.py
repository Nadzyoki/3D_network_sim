from ursina import *
import ursina.color
lines = []

def add_(vert):
    lines.append(Entity(model=Mesh(vertices=vert, mode='line',thickness = 7),color=ursina.color.cyan))