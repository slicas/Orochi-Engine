import pyray as pr
from orochi.tag import Tag
from math import *
from orochi.dir import *
from orochi.keyboard import * 
from orochi.math import *
from orochi.object import *
from orochi.alarm import *
from orochi.layer import *
import random
import colorsys

cur_dir = CLIENT_DIR


def move_4ways(object,speed,buttons = ["w","a","s","d"],rotation = False,profile = True):
    if(key_down(buttons[0])):
        object.y -= speed
    elif(key_down(buttons[2])):
        object.y += speed
    if(key_down(buttons[1])):
        object.x -= speed
        if(rotation):
            object.angle -= 1
    if(key_down(buttons[3])):
        object.x += speed
        if(rotation):
            object.angle += 1
    if(profile):
        if(not key_down(buttons[0]) and not key_down(buttons[2]) and not key_down(buttons[1]) and not key_down(buttons[3])):
            object.profile.moving = False
        else:
            object.profile.moving = True


def shake_object(object, intensity, lerp_factor=1):
    object.render_shift_x = lerp(object.render_shift_x, random.randint(-intensity, intensity), lerp_factor)
    object.render_shift_y = lerp(object.render_shift_y, random.randint(-intensity, intensity), lerp_factor)

def random_color(random_alpha = True):
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)) if random_alpha else  (random.randint(0,255),random.randint(0,255),random.randint(0,255),255)
def rainbow_color(game,speed = 1):
    hue = (game.get_steps() // int(60/speed)) % 255
    hsv_color = (hue / 255.0, 1.0, 1.0)
    rgb_color = colorsys.hsv_to_rgb(*hsv_color)
    c_rainbow = (int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))
    colour = c_rainbow
    return (colour[0],colour[1],colour[2],255)

def lerp_color(color1, color2, t):

    r1, g1, b1, a1 = color1
    r2, g2, b2, a2 = color2
    
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    a = int(a1 + (a2 - a1) * t)
    
    return r, g, b, a



def zoom_in(game,object : Object,time = 8,zoom = 1.25):
    turn_off = Alarm(time)
    def zoom_in_object():
        game.camera.not_reset = True
        game.camera.camera.target.x = lerp(game.camera.camera.target.x ,object.x,game.camera.suavity)
        game.camera.camera.target.y = lerp(game.camera.camera.target.y,object.y,game.camera.suavity)
        game.camera.camera.zoom     = lerp(game.camera.camera.zoom,zoom,game.camera.suavity)
        game.camera.camera.offset.x = lerp(game.camera.camera.offset.x,game.window_width/2,game.camera.suavity)
        game.camera.camera.offset.y = lerp(game.camera.camera.offset.y,game.window_height/2,game.camera.suavity)
        turn_off.execute()
    oZoom = object_instantiate(game,1,1,1,1,game.scene,get_layer_by_id(game.scene,"0"))
    oZoom.set_update(zoom_in_object)
    def reset():
        game.camera.not_reset = False
        oZoom.destroy()
        turn_off.active = False
    turn_off.set_function(reset)


def set_world_to_gui(gui_position,game,object):
    x,y = gui_position
    object.x = (x + game.camera.target[0])- game.camera.offset[0]
    object.y = (y +  game.camera.target[1])- game.camera.offset[1]
    return True

def set_gui_to_world(world_position,game,object):
    x, y = world_position
    object.x = (x +  game.camera.offset[0]) -  game.camera.target[0]
    object.y = (y +  game.camera.offset[1]) -  game.camera.target[1]
    return True

def return_world_to_gui(gui_position,game):
    x,y = gui_position
    return ((x + game.camera.target[0])- game.camera.offset[0],(y +  game.camera.target[1])- game.camera.offset[1])

def return_gui_to_world(world_position,game):
    x, y = world_position
    return ((x +  game.camera.offset[0]) -  game.camera.target[0],(y +  game.camera.offset[1]) -  game.camera.target[1])


def get_relative_to_gui_value(position,game):
    x, y = position
    return ((x + game.camera.offset[0]) - game.camera.target[0], (y + game.camera.offset[1]) - game.camera.target[1])

def get_relative_to_world_value(position, game):
    x,y = position
    return ((x + game.camera.target[0])-game.camera.offset[0],(y + game.camera.target[1])-game.camera.offset[0])

