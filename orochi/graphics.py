import pyray as pr
import os
from orochi.utils import *
from orochi.dir import *
cur_dir = CLIENT_DIR
Vector2 = pr.Vector2


def draw_line(point1 : Vector2,point2 : Vector2,color = (255,255,255,255),width = 1):
    pr.draw_line_ex(point1,point2,width,color)
def draw_rect(x : int,y : int,width : int,height : int,color : pr.Color,origin : int = 0,angle : float  = 0):
    pr.draw_rectangle_pro(pr.Rectangle(x,y,width,height),pr.Vector2(width*origin,height*origin),angle,color)
def draw_circle(x,y,radius,color = (255,255,255)):
    pr.draw_circle(x,y,radius,color)
def draw_text(font,text,x,y,origin = (0,0),angle = 0,fontsize = 16, spacing = 1,color = (255,255,255,255)):
    size = pr.measure_text(text,fontsize)
    pr.draw_text_pro(font,str(text),(x,y),(int(origin[0]*size),origin[1]*fontsize),angle,fontsize,spacing,color)
def draw_gui_text(game,font,text,x,y,origin = (0,0),angle = 0,fontsize = 16, spacing = 1,color = (255,255,255,255)):
    size = pr.measure_text(text,fontsize)
    x,y = return_world_to_gui((x,y),game)
    pr.draw_text_pro(font,str(text),(x,y),(origin[0]*size,origin[1]*fontsize),angle,fontsize,spacing,color)
def return_processed_image(process_list : list,image):
    img = image
    for list in process_list:
        process  = list[0]
        value = list[1]
        if(process == "BLUR"):
            pr.image_blur_gaussian(img,value)
        if(process == "GRAYSCALE"):
            pr.image_color_grayscale(img,value)
        if(process == "INVERT"):
            pr.image_color_grayscale(img,value)
    pr.image_color_replace(image,(255,0,0),pr.BLANK)
    return img

def load_texture(src):
    return pr.load_texture(f'{cur_dir}{src}')

def load_image(src):
    return pr.load_image(f'{cur_dir}'+src)

def load_font(src):
    return pr.load_font(f'{cur_dir}'+src)