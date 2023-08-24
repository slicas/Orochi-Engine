import pyray as pr
import random
import math
from orochi.math import lerp

class RectParticle:
    def __init__(self,width,height,outlined = False):
        self.width = width
        self.height = height
        self.outlined = outlined
class EllipseParticle:
    def __init__(self,radius_x,radius_y,outlined = False):
        self.radius_x = radius_x
        self.radius_y = radius_y
        self.outlined = outlined

class Particle:
    def __init__(self,game,layer,x,y,shape,min_speed,max_speed,speed_incr,color,alpha_incr,min_size,max_size,size_incr,min_dir,max_dir,dir_incr,min_angle,max_angle,angle_incr,min_life,max_life,origin):
        self.layer = layer
        self.game = game
        self.x = x
        self.y = y
        self.shape = shape
        match type(self.shape).__name__:
            case "EllipseParticle":
                self.radius_x = shape.radius_x
                self.radius_y = shape.radius_y
            case "RectParticle":
                self.width = shape.width
                self.height = shape.height
        self.shape_type = type(self.shape).__name__
        self.min_size = min_size
        self.max_size = max_size
        self.size_incr = size_incr
        self.size = self.min_size
        self.color = pr.Color(color[0],color[1],color[2],color[3])
        self.alpha_incr = alpha_incr
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.speed_incr = speed_incr
        self.speed = min_speed
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.angle_incr = angle_incr
        self.angle = min_angle
        self.min_dir = min_dir
        self.max_dir= max_dir
        self.dir = self.min_dir
        self.dir_incr = dir_incr
        self.min_life = min_life
        self.max_life = max_life
        self.life = random.uniform(min_life,max_life) + game.get_running_time()
        self.origin = origin
    def draw(self):
        match self.shape_type:
            case "RectParticle":
                if(not self.shape.outlined):
                    pr.draw_rectangle_pro(pr.Rectangle(int(self.x),int(self.y),int(self.size*self.width),int(self.size*self.height)),
                                        pr.Vector2((self.width * self.size) * self.origin, (self.height * self.size) * self.origin),self.angle,self.color)
                else:
                    pr.draw_rectangle_lines(int(self.x),int(self.y),int(self.width * self.size),int(self.height*self.size),self.color)
            case "EllipseParticle":
                if(not self.shape.outlined):
                    pr.draw_ellipse(int(self.x),int(self.y),int(self.radius_x*self.size),int(self.radius_y*self.size),self.color)
                else:
                    pr.draw_ellipse_lines(int(self.x),int(self.y),int(self.radius_x*self.size),int(self.radius_y*self.size),self.color)

    def update(self):
        if(self.dir <= self.max_dir and self.dir >= self.min_dir):
            self.dir  += self.dir_incr
        if(self.size <= self.max_size and self.size >= self.min_size):
            self.size  += self.size_incr
        if(self.angle < self.max_angle and self.angle_incr > 0):
            self.angle += self.angle_incr
        if(self.angle > self.min_angle and self.angle_incr < 0):
            self.angle += self.angle_incr
        if(self.color.a < 255 and self.alpha_incr > 0):
            self.color.a += self.alpha_incr
        if(self.color.a > 0 and self.alpha_incr < 0):
            self.color.a += self.alpha_incr
        self.x += self.speed * math.cos(math.radians(self.dir))
        self.y += self.speed * math.sin(math.radians(self.dir))

    def destroy(self):
        if(self in self.layer.get_particles()):
            self.layer.delete_particle(self)
class Emmiter:
    def __init__(self,game):
        self.game = game
        pass
    def emmit(self,game,layer,x,y,shape,min_speed,max_speed,speed_incr,color,alpha_incr,min_size,max_size,size_incr,min_dir,max_dir,dir_incr,min_angle,max_angle,angle_incr,min_life,max_life,origin):
        instance = Particle(game = game,layer = layer,x=x, y=y, shape=shape, min_speed=min_speed, max_speed=max_speed,
                            speed_incr=speed_incr, color=color, alpha_incr=alpha_incr,
                            min_size=min_size, max_size=max_size, size_incr=size_incr,
                            min_dir=min_dir, max_dir=max_dir, dir_incr=dir_incr,
                            min_angle=min_angle, max_angle=max_angle, angle_incr=angle_incr,
                            min_life=min_life,max_life=max_life,origin=origin)
        layer.add_particle(instance)

