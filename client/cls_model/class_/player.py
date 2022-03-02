from ursina import *

####################################################################
                #GUI
####################################################################
class GUI_(Entity):
    def __init__(self,parent, **kwargs):
        super().__init__()
        #point in center
        self.point_=Entity(parent = parent, model='quad', color=color.pink, scale=.01, rotation_z=45)
        # text about on you viewe now
        self.viewe = Text(text='', origin=(1, 0), color=color.green)
        ###############################################################
                        #menu
        ###############################################################
        self.mn = WindowPanel(
        title='Menu',
        content=(
            Button(text='Connecting', color=color.azure),
            Button(text='Add', color=color.azure)
        ),
        popup=False,
        enabled=False
        )
        ###############################################################
                    #Settings menu
        ###############################################################
        self.Exit_but = Button(text='Exit', color=color.azure)
        self.Exit_but.on_click = application.quit
        self.st = WindowPanel(
            title='Settings',
            content=(
                self.Exit_but,
            ),
            popup=False,
            enabled=False
        )
        ###############################################################
        # Move menu
        ###############################################################
        self.mv = ButtonGroup(('1 Connection','2 Add','3 Delete','4 Work'), min_selection=1,x=-.5,y=-.4, default='1 Connection', selected_color=color.green)
        ###############################################################
        self.menu_list = {'Esc':self.st,'Tab':self.mn,'Move':self.mv}

    def Disable_menu(self,ev):
        for i in self.menu_list.keys():
            self.menu_list[i].enabled=False
        self.menu_list[ev].enabled =True

    def TextGUI(self,text):
        self.viewe.text = text
####################################################################


class Player(Entity):
    ####################################################################
                        #Init of player
    ####################################################################
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
        self.now_state='Move'
        #move tool
        self.move_tool ={
            '1':'1 Connection',
            '2':'2 Add',
            '3':'3 Delete',
            '4':'4 Work',
        }

    ####################################################################
                    #Main update of player
    ####################################################################
    def update(self):
        match self.now_state:
            case 'Move':
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
                        #Work with statement
    ####################################################################
    def Statement(self, ev):
        if (self.now_state + ev) in self.map_event:
            return self.map_event[self.now_state + ev]

    def Chage_statement(self,ev):
        if not(ev == None):
            self.now_state=ev
            self.gui.Disable_menu(ev)
            self.on_move()

    ####################################################################
                        #Input
    ####################################################################
    def input(self, key):
        if key == 'tab':
            self.Chage_statement(self.Statement('Tab'))
        if (key == 'escape'):
            self.Chage_statement(self.Statement('Esc'))

        ####################################################################
        # Event in state of move
        ####################################################################
        if self.now_state == 'Move':
            if held_keys['shift']:
                self.speed = 4
            else:
                self.speed = 2
            #selector of mode and his actions
            if mouse.left:
                match self.gui.mv.value:
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
                self.gui.mv.value = self.move_tool[key]


    ####################################################################
                        #Walk
    ####################################################################
    def on_move(self):
        mouse.locked = not(mouse.locked)

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
