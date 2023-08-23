import math
import random 
from noise import snoise2
from perlin_noise import PerlinNoise
import numpy
from pygame import math as pgmath
from pyray import Vector2 as v2
random = random
math = math
numpy = numpy
gmath = pgmath

Vector2 = v2

class Ellipse:
    def __init__(self,center_x,center_y,radius_x,radius_y):
        self.center_x = center_x
        self.center_y = center_y
        self.radius_x = radius_x
        self.radius_y = radius_y




def angle_difference(dest, src):
    diff = (dest - src + 180) % 360 - 180
    return diff


def point_distance(point1 : Vector2, point2 : Vector2):
    dx = point2.x - point1.x
    dy = point2.y - point1.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance

def point_direction(point1 : Vector2,point2 : Vector2):
  

  dx = point2.x - point1.x
  dy = point2.y - point1.y
  direction = math.atan2(dy, dx)
  direction = direction * 180 / math.pi
  if direction < 0:
    direction += 360
  return direction



def lerp(a, b, amt):
    return a + amt * (b - a)

def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def simplex_noise_1d_list(width,scale = 50,octaves = 10,persistence = .8,lacunarity = 2,seed = random.randint(-999999999,999999999)):
    noise = []
    for x in range(1,width):
        value = snoise2(x/scale,1/scale,octaves,persistence,lacunarity,seed)
        noise.append(value)
    return noise

def simplex_noise_1d_value(x,scale = 50,octaves = 10,persistence = .8,lacunarity = 2,seed = random.randint(-999999999,999999999)):
    return snoise2(x/scale,1/scale,octaves,persistence,lacunarity,seed)



def simplex_noise_2d_list(width,height,scale = 50,octaves = 10,persistence = .8,lacunarity = 2,seed = random.randint(-999999999,999999999)):
    noise = []
    for y in range(height):
        for x in range(width):
            value = snoise2(x/scale,y/scale,octaves,persistence,lacunarity,seed)
            noise.append(value)
    return noise

def simplex_noise_2d_value(x,y,scale = 50,octaves = 10,persistence = .8,lacunarity = 2,seed = random.randint(-999999999,999999999)):
    return snoise2(x/scale,y/scale,octaves,persistence,lacunarity,seed)

def perlin_noise_1d_value(x,scale = 50,octaves = 10,seed = random.randint(-999999999,999999999)):
    noise = PerlinNoise(octaves,seed)
    return noise((x/scale,1/scale))

def perlin_noise_1d_list(width,scale = 50,octaves = 10,seed = random.randint(-999999999,999999999)):
    noise = []
    perlin = PerlinNoise(octaves,seed)
    for x in range(width):
        noise.append(perlin((x/scale,1/scale)))
    return noise

def perlin_noise_2d_value(x,y,scale = 50,octaves = 10,seed = random.randint(-999999999,999999999)):
    noise = PerlinNoise(octaves,seed)
    return noise((x/scale,y/scale))

def perlin_noise_2d_list(width,height,scale = 50,octaves = 10,seed = random.randint(-999999999,999999999)):
    noise = []
    perlin = PerlinNoise(octaves,seed)
    for y in range(height):
        for x in range(width):
            noise.append(perlin((x/scale,y/scale)))
    return noise

