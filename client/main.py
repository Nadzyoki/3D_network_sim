from ursina import *
from cls_model.room import *

def main():
    main_menu = Ursina()
    window.title = 'ursina'
    pool_main_menu = []
    title = Text(text=dedent("<scale:2><azure>Simulation of Network in 3D"),
               position=window.top_left,
               origin=Vec2(-.5,2)
               )
    bl = ButtonList(button_dict=button_dict, position=window.left, button_height=1)
    pool_main_menu.append(title)
    pool_main_menu.append(bl)

    room = Room()
    button_dict = {
        'Start': Func(Start,room,pool_main_menu),
        'two': None,
        'Setting': None,
        'Exit': application.quit,
    }
    window.color = color._32
    main_menu.run()

def Start(room,pool):
    for i in pool:
        i.enabled = False
    room.Start()

if __name__ == "__main__":
    main()