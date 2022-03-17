from ursina import *

def Logo():
    camera.overlay.color = color.black
    logo = Sprite(name='ursina_splash', parent=camera.ui, texture='cisco', world_z=camera.overlay.z-1, scale=.4, color=color.clear)
    logo.animate_color(color.white, duration=2, delay=1, curve=curve.out_quint_boomerang)
    camera.overlay.animate_color(color.clear, duration=1, delay=4)
    destroy(logo, delay=5)

    def splash_input(key):
        destroy(logo)
        camera.overlay.animate_color(color.clear, duration=.25)

    logo.input = splash_input
