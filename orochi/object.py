import pyray as pr
from orochi.tag import tag_store
import types
import orochi.math
from orochi.scene import *
from orochi.layer import *

class Profile:
    def __init__(self):
        pass

class CollisionBody:
    def __init__(self,object,ID : str,type : str,width = 1,height = 1,radius_x = 1,radius_y = 1,x_shift = 0,y_shift = 0):
        self.object = object
        self.width = width
        self.height = height
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.x = self.object.x + self.x_shift
        self.y = self.object.y + self.y_shift
        self.origin = object.origin
        self.__type = type
        self.body = pr.Rectangle(self.x,self.y,self.width,self.width) if self.__type == "QUAD" else orochi.math.Ellipse(self.x,self.y,self.radius_x,self.radius_y)
        self.ID = ID
    def get_type(self):
        return self.__type
    def show_collision_shape(self):
        match self.__type:
            case "QUAD" : pr.draw_rectangle_lines(self.x,self.y,self.width,self.height,(0,255,0,255))
            case "ELLIPSE" : pr.draw_ellipse_lines(self.x,self.y,self.radius_x,self.radius_y,(0,255,0,255))
    def update(self):
        match self.__type:
            case "QUAD":
                self.origin = self.object.origin
                self.x = int((self.object.x - (self.width*self.origin))+ self.x_shift)
                self.y = int((self.object.y - (self.height*self.origin)) + self.y_shift)
                self.body = pr.Rectangle(self.x,self.y,self.width,self.width)
            case "ELLIPSE":
                self.origin = self.object.origin
                self.x = int((self.object.x - (self.width*self.origin))+ self.x_shift)
                self.y = int((self.object.y - (self.height*self.origin)) + self.y_shift)
                self.body = orochi.math.Ellipse(self.x,self.y,self.radius_x,self.radius_y)
class Object:
    def __init__(self,game,x,y,width,height,image = None,name = "unamed",begin_with_collision_body = False):
        self.game = game
        self.x = x
        self.y = y
        self.x_scale = 1
        self.y_scale = 1
        self.__layer = None
        self.__scene = None
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
        self.origin = 0.0
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
        self.render_shift_x = 0
        self.render_shift_y = 0
        if(image != None):
            self.frame_width = self.image.width
            self.frame_height = self.image.height
        else:
            self.frame_width = 0
            self.frame_height = 0

    def reset_render_shift(self):
        self.render_shift_x = 0
        self.render_shift_y = 0
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
    def set_update(self,update):
        if(isinstance(update,types.FunctionType) or isinstance(update,types.MethodType)):
            self.__update = update
    def set_draw(self,draw):
        if(isinstance(draw,types.FunctionType) or isinstance(draw,types.MethodType)):
            self.__draw = draw
    def get_update(self):
        if(self.__update != None):
            self.__update(self)
    def get_draw(self):
        if(self.__draw != None):
            self.__draw(self)
    def get_layer(self):
        return self.__layer
    def set_layer(self,new_layer):
        for layer in self.game.scene.layers:
            if(layer == self.__layer and self in layer.get_objects()):
                layer.remove(self)
        self.__layer = new_layer
        self.__layer.add(self)
        return True
    def destroy(self):
        self.get_layer().delete(self)
        self.__scene.objects.remove(self)
        self.scene = None
        self.layer = None
        self.destroyed = True
        for tag in self.tags:
            if(self in tag.get_objects()):
                tag.delete(self)
        self.tags = []
        self.game.len_objects -= 1

    def render(self):
        if(self.animation):
            self.animation.play(self.animation_speed,self)
        if(self.image != None):
            flip_x = 1 if self.x_scale >= 1 else -1
            flip_y = 1 if self.y_scale >= 1 else -1
            pr.set_texture_filter(self.image,pr.TextureFilter.TEXTURE_FILTER_ANISOTROPIC_8X)
            pr.draw_texture_pro(self.image,pr.Rectangle(self.frame_x,self.frame_y,self.frame_width*flip_x,self.frame_height*flip_y),pr.Rectangle(self.x + self.render_shift_x,self.y + self.render_shift_y,self.width*abs(self.x_scale),self.height*abs(self.y_scale)),pr.Vector2((self.width * abs(self.x_scale))*self.origin, (self.height*abs(self.y_scale))*self.origin),self.angle,self.tint)
    def get_id(self):
        return self.__ID
    def in_scene(self,scene: Scene = None,layer : Layer = None):
        scene = self.game.scene if scene == None else scene
        layer = get_layer_by_id(scene,"0") if layer == None else layer
        self.__scene = scene
        self.__scene.objects.append(self)
        self.set_layer(layer)
        self.destroyed = False
        self.__ID = self.game.len_objects


def object_instantiate(game,x,y,width,height,scene = None,layer = None,image = None,tags = [],origin = 0,tint = pr.WHITE,angle = 0,update = None,draw = None):
        object = Object(game,x,y,width,height,image)
        object.in_scene(scene,layer)
        object.origin = origin
        object.tint = tint
        object.angle = angle
        if(len(tags) > 0):
            for tag in tags:
                if(isinstance(tag,str)):
                    for tag_name in tag_store.tags:
                        if(tag == tag_name.get_name()):
                            tag_name.add(object)
                else:
                    tag.add(object)
        if(update):
            object.set_update(update)
        if(draw):
            object.set_draw(draw)
        return object

def instance_model(game,x,y,width,height,scene = None,layer = None,image = None,tags = [],origin = 0,tint = pr.WHITE,angle =0,update = None,draw = None):
    return {"game":game,"x":x,"y":y,"scene":scene,"width":width,"height":height,"image":image,"layer":layer,"tags":tags,"origin":origin,"tint":tint,"angle":angle,"update":update,"draw":draw}
