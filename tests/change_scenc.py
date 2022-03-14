from ursina import *

class Scene1(Ursina):
    def __init__(self):
        super().__init__()
        self.t = Text(text="1")


class Scene2(Ursina):
    def __init__(self):
        super().__init__()
        Text(text="2")

if __name__ == '__main__':

    while True:
        g = int(input("enter s"))
        if g == 1:
            base =Scene1()
            print(base.child)
        if g == 2:
            base =Scene2()
            print(base)
        base.destroy()