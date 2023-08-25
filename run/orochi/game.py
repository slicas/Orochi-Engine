print("""
Special thanks to: \n

Raylib: https://github.com/raysan5/raylib \n

Lapce: https://github.com/lapce/lapce \n


            
      """)


import pyray as pr
from orochi.scene import Scene
from orochi.graphics import *
from orochi.community import *
from orochi.camera import Camera
from orochi.mouse import *
import sys
import types
from orochi.dir import *
import traceback
from orochi.alert import ERROR
import time
cur_dir = ENGINE_DIR

class Game:
    def __init__(self,window_width = 500,window_height = 500,window_title = "Made with Orochi",window_icon = None,resizable = False):
        self.window_width = window_width
        self.window_height = window_height
        self.window_title = window_title
        self.clear_color = (25, 25, 25, 255)
        self.raylib = pr
        self.closed = pr.window_should_close
        self.resizable = resizable
        self.len_objects = 0
        self.camera = Camera((0,0))
        self.__running = True
        self.fps_target = 60
        self.ws_conn = None
        self.__init_time = time.time()
        self.__time = 0
        self.fps = 0
        self.musics = []
        self.sound_instances = []
        self.animations = []
        self.scenes = []
        self.alarms = []
        self.particles = []
        self.gui_components = []
        self.__steps = 0
        self.scene = Scene("0",self,self.window_width,self.window_height)
        self.physics = None
        self.__update = None
        self.__gui_draw= None
        self.__on_exit = None
        self.frame = 1
        if(window_icon == None):
                self.window_icon = pr.load_image(f'{ENGINE_DIR}/src/orochi_icon.png')
        else:
             self.window_icon = window_icon
    @property
    def running(self):
        return self.__running
    def set_on_exit_function(self,function):
        self.__on_exit = function
        return True
    def set_update(self,update):
        if(isinstance(update,types.FunctionType) or isinstance(update,types.MethodType)):
            self.__update = update
    def set_gui_draw(self,gui_draw):
        if(isinstance(gui_draw,types.FunctionType) or isinstance(gui_draw,types.MethodType)):
            self.__gui_draw = gui_draw
    def init(self):
        if(self.resizable):
            pr.set_config_flags(pr.ConfigFlags.FLAG_WINDOW_RESIZABLE)
        pr.init_window(self.window_width,self.window_height,self.window_title)
        pr.init_audio_device()   
        pr.set_window_icon(self.window_icon)
        pr.set_target_fps(self.fps_target)

    def toggle_fullscreen(self):
        pr.toggle_fullscreen()
    def hide_cursor(self):
        pr.disable_cursor()
    def show_cursor(self):
        pr.enable_cursor()
    def get_steps(self):
        return self.__steps
    def close(self):
        pr.enable_cursor()
        self.__running = False
        if(self.__on_exit):
            self.__on_exit()
        if(self.ws_conn):
            self.ws_conn.close()
            pass
        pr.close_audio_device()
        pr.close_window()
        sys.exit()
    def awalys_on_top(self,state = True):
        if(state):
            pr.set_window_state(pr.ConfigFlags.FLAG_WINDOW_TOPMOST)
        else:
            pr.clear_window_state(pr.ConfigFlags.FLAG_WINDOW_TOPMOST) 
    def get_running_time(self):
        return self.__time
    def looping(self):
        try:
            change_cursor(DEFAULT_CURSOR)
            
            self.__time = time.time() - self.__init_time
            self.window_width = pr.get_screen_width()
            self.window_height = pr.get_screen_height()
            self.fps = pr.get_fps()
            self.__steps += 1
            if self.physics is not None and self.fps != 0:
                self.physics.world.step(1 / self.fps_target)

            if self.closed():
                self.close()
            for music in self.musics:
                pr.update_music_stream(music)

            pr.begin_drawing()
            pr.clear_background(self.clear_color)

            pr.begin_mode_2d(self.camera.camera)
            if(self.camera.not_reset == False):
                self.camera.reset_angle()
                self.camera.reset_offset()
                self.camera.reset_target()
                self.camera.reset_zoom()

    
            if self.__update:
                self.__update()
            for layer in self.scene.layers:
                if layer.get_id() != "GUI":
                    for object in layer.get_objects():
                        if not object.destroyed:
                            object.x += object.speed * math.cos(math.radians(object.direction))
                            object.y += object.speed * math.sin(math.radians(object.direction))
                            object.get_draw()
                            object.get_update()
                            object.render()
                            for body in object.get_all_collisions_bodies():
                                body.update()
                    for particle in layer.get_particles():
                        if(self.get_running_time() < particle.life):
                            particle.update()
                            particle.draw()
                        else:
                            particle.destroy()

            pr.end_mode_2d()

            for layer in self.scene.layers:
                if layer.get_id() == "GUI":
                    for object in layer.get_objects():
                        if not object.destroyed:
                            object.x += object.speed * math.cos(math.radians(object.direction))
                            object.y += object.speed * math.sin(math.radians(object.direction))
                            object.get_draw()
                            object.get_update()
                            object.render()
                            for body in object.get_all_collisions_bodies():
                                body.update()
                    for particle in layer.get_particles():
                        if(self.get_running_time() < particle.life):
                            particle.update()
                            particle.draw()
                        else:
                            particle.destroy()
            for component in self.gui_components:
                component.render()
                component.update()

            if(self.__gui_draw):
                self.__gui_draw()

            pr.end_drawing()
            for alarm in self.alarms:
                alarm.start(self)
            
        except Exception as e:
            if(ERROR(e,traceback.format_exc()) == "Exit"):
                self.close()

            

