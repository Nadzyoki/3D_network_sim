from ursina import *
from .state_mach import State_machine

class GUI_(Entity):
    def __init__(self,parent, **kwargs):
        super().__init__()
        self.point_=Entity(parent = parent, model='quad', color=color.pink, scale=.01, rotation_z=45)
        # text about on you viewe now
        self.viewe = Text(text='', origin=(1, 0), color=color.green)
        self.state = Text(text='', origin=(12,12), color=color.cyan)
        self.mn = WindowPanel(
        title='Menu',
        content=(
            Button(text='Connecting', color=color.azure),
            Button(text='Add', color=color.azure)
        ),
        popup=True,
        enabled=False
        )
        self.st = WindowPanel(
            title='Settings',
            content=(
                Button(text='Exit', color=color.azure),
            ),
            popup=True,
            enabled=False
        )

    def TextGUI(self,text):
        self.viewe.text = text

    def State(self,text):
        self.state.text = text

    def Menu(self):
        self.mn.enabled = not(self.mn.enabled)

    def Settings(self):
        self.st.enabled = not (self.st.enabled)



class Player(Entity):
    def __init__(self, **kwargs):
        self.gui = GUI_(parent=camera.ui)
        super().__init__()
        self.speed = 1
        self.height = 2
        self.camera_pivot = Entity(parent=self, y=self.height)

        camera.parent = self.camera_pivot
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90
        mouse.locked = True
        self.mouse_sensitivity = Vec2(40, 40)

        self.dis_v=1
        self.hit_info=raycast(origin=camera, direction=camera.forward, ignore=(self,), distance=self.dis_v)

        for key, value in kwargs.items():
            setattr(self, key ,value)
        #state of choise
        self.map_event = {

        'MoveEsc': 'Esc',
        'MoveTab': 'Tab',

        'TabTab': 'Move',

        'EscEsc': 'Move',
        }
        self.state = State_machine(self.map_event,'Move')

    def update(self):
        match self.state.now:
            case 'Move':
                self.gui.TextGUI(self.name_of_viewe())
                self.gui.State(str(self.state.now))
                self.move_pl()
                self.hit_info = raycast(origin=camera, direction=camera.forward, ignore=(self,), distance=self.dis_v)
                # self.on_enable()
            case 'Tab':
                self.gui.State('Menu')
            case 'Esc':
                self.gui.State('Settings')

    def viewe(self):
        if self.hit_info.hit:
            return True

    def name_of_viewe(self):
        if self.viewe():
            # print(obf.name,obf.world_position,obf.parent)
            return self.hit_info.entity.name

    def vec_of_viewe(self):
        if self.viewe():
            return self.hit_info.entity.world_position

    def actv_of_viewe(self):
        if self.viewe() and (self.hit_info.entity.activable == True):
            self.hit_info.entity.Actived()

    def input(self, key):
        if key == 'tab':
            self.state.Event('Tab')
        if (key == 'escape'):
            self.state.Event('Esc')
        # speed up
        if held_keys['shift']:
            self.speed=4
        else :
            self.speed=2

        if self.state.now == 'Move':

            if mouse.left:
                if hasattr(self.hit_info.entity,'activable'):
                    self.actv_of_viewe()


    def on_move(self):
        mouse.locked = not(mouse.locked)


    #move and vector of viewe
    def move_pl(self):
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)

        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()

        feet_ray = raycast(self.position + Vec3(0, 0.5, 0), self.direction, ignore=(self,), distance=.5, debug=False)
        head_ray = raycast(self.position + Vec3(0, self.height - .1, 0), self.direction, ignore=(self,), distance=.5,debug=False)

        if not feet_ray.hit and not head_ray.hit:
            self.position += self.direction * self.speed * time.dt

        raycast(self.world_position + (0, self.height, 0), self.down, ignore=(self,))