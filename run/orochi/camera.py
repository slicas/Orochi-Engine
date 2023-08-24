import pyray as pr
from orochi.math import lerp,perlin_noise_1d_value
import random
class Camera:
    def __init__(self,offset : tuple,zoom : float = 1.0,angle : float = 0.0,target : tuple = (0,0),suavity = 1):
        self._offset = offset
        self._zoom = zoom
        self._angle = angle
        self._real_target = target
        self._target = target
        self.suavity = suavity
        self.camera = pr.Camera2D(self._offset,self._target,self._angle,self._zoom)
        self.__perlin_usage = 1
        self.not_reset = False
    def follow(self,object):
        x,y = self._target
        self._real_target = (object.x,object.y)
        self._target = (lerp(x ,object.x,self.suavity),lerp(y ,object.y,self.suavity))
        self.camera = pr.Camera2D(self._offset,self._target,self._angle,self._zoom)
    def reset_angle(self):
        self.camera.rotation = lerp(self.camera.rotation,self.angle,self.suavity)
    def reset_offset(self):
        self.camera.offset.x = lerp(self.camera.offset.x,self.offset[0],self.suavity)
        self.camera.offset.y = lerp(self.camera.offset.y,self.offset[1],self.suavity)
    def reset_target(self):
        self.camera.target.x = lerp(self.camera.target.x,self.target[0],self.suavity)
        self.camera.target.y = lerp(self.camera.target.y,self.target[1],self.suavity)
    def reset_zoom(self):
        self.camera.zoom = lerp(self.camera.zoom,self.zoom,self.suavity)

    @property
    def offset(self):
        return self._offset
    @offset.setter
    def offset(self,value):
        self._offset = (lerp(self._offset[0],value[0],self.suavity),lerp(self._offset[1],value[1],self.suavity))
        self.camera = pr.Camera2D(self.offset,self.target,self.angle,self.zoom)
    @property
    def angle(self):
        return self._angle
    @angle.setter
    def angle(self,value):
        self._angle = value
        self.camera = pr.Camera2D(self.offset,self.target,self.angle,self.zoom)
    
    @property
    def zoom(self):
        return self._zoom
    @zoom.setter
    def zoom(self,value):
        self._zoom = value
        self.camera = pr.Camera2D(self.offset,self.target,self.angle,self.zoom)

    @property
    def target(self):
        return self._target
    @target.setter
    def target(self,value):
        x,y = self.target
        self._real_target = (value[0],value[1])
        self._target = (lerp(x,value[0],self.suavity),lerp(y,value[1],self.suavity))
        self.camera = pr.Camera2D(self.offset,self.target,self.angle,self.zoom)
    
    @property
    def real_target(self):
        return self._real_target
    
    def apply_screen_shake(self,intensity = 10,rotation = True,type = "Normal"):
        if type == "Normal":
            self.camera.offset.x += random.uniform(-intensity, intensity)
            self.camera.offset.y += random.uniform(-intensity, intensity)
            if(rotation):
                shake_angle = random.uniform(-intensity, intensity)
                self.camera.rotation -= shake_angle

        elif type == "Perlin":
            self.__perlin_usage += 1
            v = self.__perlin_usage 
            self.camera.offset.x += perlin_noise_1d_value(v,seed=662)* intensity
            self.camera.offset.y += perlin_noise_1d_value(v,seed=662)* intensity
            if(rotation):
                shake_angle = perlin_noise_1d_value(v,seed=664)* intensity
                self.camera.rotation -= shake_angle



