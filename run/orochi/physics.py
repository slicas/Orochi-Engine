import pymunk
import pyray as pr
from orochi.object import CollisionBody,Profile
from orochi.alert import alert
import types


print("Caution!!","""
    The physics module of the Orochi Engine is under development and is currently unstable. It is not recommended to use it in final versions of any projects.
""")

class Physics:
    def __init__(self,world_gravity):
        self.world_gravity = world_gravity
        self.world = pymunk.Space()
        self.world.gravity = self.world_gravity[0],self.world_gravity[1]
    def set_gravity(self,gravity:tuple):
        self.world.gravity = gravity[0],gravity[1]


class PhysicsObject:
    def __init__(self, game, x, y, width, height, image, name,begin_with_collision_body):
        self.game = game
        self.x = x
        self.y = y
        self.x_scale = 1
        self.y_scale = 1
        self.__layer = "0" 
        self.scene = None
        self.width = width
        self.height = height
        self.__image = image
        self.frame = 0
        self.__animation = None
        self.__ID = None
        self.game.len_objects += 1
        self.tags = []
        self.tint = pr.WHITE
        self.angle = 0
        self.origin = 0.5 
        self.__collisions_bodies = [CollisionBody(self,"Body","QUAD",width = self.width,height = self.height)] if begin_with_collision_body else []
        self.destroyed = False
        self.animation_speed = 1
        self.__update = None
        self.__draw = None
        self.frame_x = 0
        self.frame_y = 0
        self.direction = 0
        self.speed = 0
        self.profile = Profile()
        self.destroyed = False
        self.settings = None
    def get_all_collisions_bodies(self):
        return self.__collisions_bodies
    def get_collision_body(self,ID):
        for body in self.__collisions_bodies:
            if(body.ID == ID):
                return body
    def add_collision_body(self,collision_body):
        self.__collisions_bodies.append(collision_body)
    def remove_collision_body(self,collision_body):
        self.__collisions_bodies.remove(collision_body)
    def show_all_collisions_bodies(self):
        for collision in self.__collisions_bodies:
            collision.show_collision_shape()
    def body_update(self):
        self.x, self.y = self.body.position
        self.angle = self.body.angle * 180 / 3.14159265359
    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self,image):
        self.__image = image
        if(self.animation == None):
            self.frame = 0
            self.frame_x = 0
            self.frame_y = 0
            self.frame_width = image.width
            self.frame_height = image.height
    @property
    def animation(self):
        return self.__animation
    @animation.setter
    def animation(self,animation):
        if(self.__animation != animation):
            self.__animation = animation
            self.frame = 0
    def position(self):
        return pr.Vector2(self.x,self.y)
    def get_update(self):
        if(self.__update != None):
            self.__update()
    def get_draw(self):
        if(self.__draw != None):
            self.__draw()
    def get_layer(self):
        return self.__layer
    def set_layer(self,new_layer : str):
        for layer in self.scene.layers:
            if(layer.get_id() == self.__layer and self in layer.get_objects()):
                layer.remove(self)
        self.__layer = new_layer
        for layer in self.scene.layers:
            if(layer.get_id() == self.__layer and not self in layer.get_objects()):
                layer.add(self)
        return True
    def set_update(self,update):
        if(isinstance(update,types.FunctionType) or isinstance(update,types.MethodType)):
            self.__update = update
    def set_draw(self,draw):
        if(isinstance(draw,types.FunctionType) or isinstance(draw,types.MethodType)):
            self.__draw = draw
    def destroy(self):
        try:
            for scene in self.game.scenes:
                if(scene.get_id() == self.scene.get_id()):
                    for layer in scene.layers:
                        if(layer.get_id() == self.layer.get_id()):
                            layer.remove(self)
                            scene.objects.remove(self)
                            self.scene = None
                            self.layer = None
                            self.destroyed = True
                            for tag in self.tags:
                                tag.delete(self)
                            self.game.len_objects -= 1
                            self.game.physics.world.remove(self.settings)
        except:
            pass
    def render(self):
        if(self.animation):
            self.animation.play(self.animation_speed,self)
        if(self.image != None):
            flip_x = 1 if self.x_scale >= 1 else -1
            flip_y = 1 if self.y_scale >= 1 else -1
            pr.set_texture_filter(self.image,pr.TextureFilter.TEXTURE_FILTER_ANISOTROPIC_8X)
            pr.draw_texture_pro(self.image,pr.Rectangle(self.frame_x,self.frame_y,self.frame_width*flip_x,self.frame_height*flip_y),pr.Rectangle(self.x,self.y,self.width*abs(self.x_scale),self.height*abs(self.y_scale)),pr.Vector2((self.width * abs(self.x_scale))*self.origin, (self.height*abs(self.y_scale))*self.origin),self.angle,self.tint)
    def get_id(self):
        return self.__ID
    def in_scene(self,scene_id = "0",layer_id = "0"):
        for scene in self.game.scenes:
            if(scene.get_id() == scene_id):
                scene.objects.append(self)
                self.scene = scene
                for layer in scene.layers:
                    if(layer.get_id() == layer_id):
                        layer.add(self)
                        self.layer = layer
                        self.destroyed = False
                        self.__ID = self.game.len_objects
                        self.game.physics.world.add(self.body,self.settings)
                        
class DynamicObject(PhysicsObject):
    def __init__(self, game, x, y, width, height, image=None, name="unamed",begin_with_collision_body = False,mass=1):
        super().__init__(game, x, y, width, height, image, name,begin_with_collision_body)  # Chamar o init da classe base
        self.mass = mass
        self.body = pymunk.Body(mass, pymunk.moment_for_box(mass, (self.width, self.height)))
        self.body.position = (self.x, self.y)
        self.settings = pymunk.Poly.create_box(self.body, (self.width, self.height))
    def get_all_collisions_bodies(self):
            return super().get_all_collisions_bodies()
    def get_collision_body(self, ID):
        return super().get_collision_body(ID)
    def add_collision_body(self, collision_body):
        return super().add_collision_body(collision_body)
    def body_update(self):
        return super().body_update()
    def update(self, method):
        return super().update(method)
    def destroy(self):
        return super().destroy()
    def render(self):
        return super().render()
    def get_id(self):
        return super().get_id()
    def in_scene(self, scene_id="0", layer_id="0"):
        return super().in_scene(scene_id, layer_id)
    def position(self):
        return super().position()
    def impulse(self,x,y):
        self.body.apply_impulse_at_local_point((x,y))
    def force(self,x,y):
        self.body.apply_force_at_local_point((x,y))
    def velocity_x(self, x_speed):
        current_vx, current_vy = self.body.velocity
        self.body.velocity = x_speed, current_vy
    def velocity_y(self, y_speed):
        current_vx, current_vy = self.body.velocity
        self.body.velocity = current_vx, y_speed
    def set_draw(self, draw):
        return super().set_draw(draw)
    def set_layer(self, new_layer: str):
        return super().set_layer(new_layer)
    def set_update(self, update):
        return super().set_update(update)
        
class StaticObject(PhysicsObject):
    def __init__(self, game, x, y, width, height, image=None, name="unamed",begin_with_collision_body = False):
        super().__init__(game, x, y, width, height, image, name, begin_with_collision_body)  # Chamar o init da classe base
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (self.x, self.y)
        self.settings = pymunk.Poly.create_box(self.body, (self.width, self.height))
    def get_all_collisions_bodies(self):
        return super().get_all_collisions_bodies()
    def get_collision_body(self, ID):
        return super().get_collision_body(ID)
    def add_collision_body(self, collision_body):
        return super().add_collision_body(collision_body)
    def body_update(self):
        return super().body_update()
    def update(self, method):
        return super().update(method)
    def destroy(self):
        return super().destroy()
    def render(self):
        return super().render()
    def get_id(self):
        return super().get_id()
    def in_scene(self, scene_id="0", layer_id="0"):
        return super().in_scene(scene_id, layer_id)
    def position(self):
        return super().position()
    def set_draw(self, draw):
        return super().set_draw(draw)
    def set_layer(self, new_layer: str):
        return super().set_layer(new_layer)
    def set_update(self, update):
        return super().set_update(update)
