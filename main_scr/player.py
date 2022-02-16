from ursina import *

class GUI_(Entity):
    def __init__(self,parent, **kwargs):
        super().__init__()
        self.point_=Entity(parent = parent, model='quad', color=color.pink, scale=.01, rotation_z=45)
        # text about on you viewe now
        self.viewe = Text(text='', origin=(1, 0), color=color.green)
        self.state = Text(text='', origin=(12,12), color=color.cyan)

    def TextGUI(self,text):
        self.viewe.text = text

    def State(self,text):
        self.state.text = text



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

        self.gravity = 1
        self.grounded = False
        self.jump_height = 2
        self.jump_up_duration = .5
        self.fall_after = .35 # will interrupt jump up
        self.jumping = False
        self.air_time = 0



        self.dis_v=1
        self.hit_info=raycast(origin=camera, direction=camera.forward, ignore=(self,), distance=self.dis_v)

        for key, value in kwargs.items():
            setattr(self, key ,value)

        # make sure we don't fall through the ground if we start inside it
        if self.gravity:
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            if ray.hit:
                self.y = ray.world_point.y

    #     state of choise
        self.state = True
        self.menu = False



    def update(self):
        if not(self.menu):
            self.gui.TextGUI(self.name_of_viewe())
            self.gui.State(str(self.state))

            self.move_pl()
            self.hit_info = raycast(origin=camera, direction=camera.forward, ignore=(self,), distance=self.dis_v)



    def viewe(self):
        if self.hit_info.hit:
            return True

    def name_of_viewe(self):
        if self.viewe():
            obf = self.hit_info.entity
            # print(obf.name,obf.world_position,obf.parent)
            return obf.name

    def vec_of_viewe(self):
        if self.viewe():
            return self.hit_info.entity.world_position

    def actv_of_viewe(self):
        if self.viewe() and (self.hit_info.entity.activable == True):
            self.hit_info.entity.Actived()

    def input(self, key):
        if key == 'space':
            self.jump()

        if key == 'tab':
            self.state = not(self.state)
        # speed up
        if held_keys['shift']:
            self.speed=4
        else :
            self.speed=2

        if self.state:
            # color of wieve
            if mouse.left:
                self.actv_of_viewe()

        # elif self.state == 2:

    def on_enable(self):
        mouse.locked = True
        self.gui.enabled = True

    def on_disable(self):
        mouse.locked = False
        self.gui.enabled = False

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

        if self.gravity:
            # gravity
            ray = raycast(self.world_position + (0, self.height, 0), self.down, ignore=(self,))

            if ray.distance <= self.height + .1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5:  # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False
            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance - .05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity

    def start_fall(self):
        self.y_animator.pause()
        self.jumping = False

    def land(self):
        self.air_time = 0
        self.grounded = True

    def jump(self):
        if not self.grounded:
            return
        self.grounded = False
        self.animate_y(self.y+self.jump_height, self.jump_up_duration, resolution=int(1//time.dt), curve=curve.out_expo)
        invoke(self.start_fall, delay=self.fall_after)

