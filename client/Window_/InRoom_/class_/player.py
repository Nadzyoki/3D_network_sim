from ursina import *

####################################################################
                #GUI
####################################################################
class GUI_(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        # text about on you viewe now
        self.viewe = Text(text='', origin=(1, 0), color=color.green)

    def TextGUI(self,text):
        self.viewe.text = text
####################################################################


class Player(Entity):
    ####################################################################
                        #Init of player
    ####################################################################
    def __init__(self,scn, **kwargs):
        super().__init__()

        self.scene = scn
        self.gui = GUI_(parent=camera.ui)
        self.scene.pool.append(self.gui)
        self.point = Entity(parent=camera.ui, model='quad', color=color.pink, scale=.01, rotation_z=45)
        self.scene.pool.append(self.point)
        self.mv = ButtonGroup(('1 Connection', '2 Add', '3 Delete', '4 Work'), min_selection=1, x=-.5, y=-.4,
                              default='1 Connection',
                              selected_color=color.green,
                              parent=self
                              )

        self.speed = 1
        self.height = 2
        self.camera_pivot = Entity(parent=self, y=self.height)
        self.p_l = PointLight(parent=self, color=color.white, position=(0, 10, -1, 5))
        # self.scene.pool.append(self.p_l)

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
        self.move_tool ={
            '1':'1 Connection',
            '2':'2 Add',
            '3':'3 Delete',
            '4':'4 Work',
        }

    ####################################################################
                    #MAIN update of player
    ####################################################################
    def update(self):
        self.gui.TextGUI(self.name_of_viewe())
        self.move_pl()
        self.hit_info = raycast(origin=camera, direction=camera.forward, ignore=(self,), distance=self.dis_v)


    ####################################################################
                    #This for actived and receiving name of object
    ####################################################################
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

    ####################################################################
                        #Input
    ####################################################################
    def input(self, key):
        ####################################################################
        # Event in state
        ####################################################################
        if held_keys['shift']:
            self.speed = 4
        else:
            self.speed = 2
        #selector of mode and his actions
        if mouse.left:
            match self.mv.value:
                case '1 Connection':
                    if hasattr(self.hit_info.entity,'activable'):
                        self.actv_of_viewe()
                case '2 Add':
                    pass
                case '3 Delete':
                    pass
                case '4 Work':
                    pass

        if key in ['1','2','3','4']:
            self.mv.value = self.move_tool[key]


    ####################################################################
                        #Walk
    ####################################################################
    # def on_move(self):
    #     mouse.locked = not(mouse.locked)

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
    ####################################################################

####################################################################
            #Connection tool
####################################################################
class Connection_tool:
    def __init__(self, mach):
        self.One = None
        self.Two = None
        self.Machine = mach

    def Connect(self, address):
        if self.One == None:
            self.One = address
        elif self.Two == None:
            self.Two = address
            self.Send()

    def Send(self):
        self.Machine.connect_ports(self.One, self.Two)
        self.One = None
        self.Two = None

####################################################################
