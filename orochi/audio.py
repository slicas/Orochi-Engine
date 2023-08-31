import pyray as pr
from orochi.game import Game
from orochi.dir import *



cur_dir = CLIENT_DIR
class Music:
    def __init__(self,game : Game,src,looping = False,pitch = 1,pan = 0.5,volume = 100):
        self.game = game
        self.music = pr.load_music_stream(f'{cur_dir}{src}')
        pr.set_music_pitch(self.music,pitch)
        pr.set_music_volume(self.music,volume/100)
        pr.set_music_pan(self.music,pan)
        self.music.looping = looping
    def set_pitch(self,pitch):
        pr.set_music_pitch(self.music,pitch)
    def set_volume(self,volume):
        pr.set_music_volume(self.music,volume/100)
    def set_pan(self,pan):
        pr.set_music_pan(self.music,pan)
    def play(self):
        pr.play_music_stream(self.music)
        if(not self.music in self.game.musics):
            self.game.musics.append(self.music)
    def stop(self):
        pr.stop_music_stream(self.music)
        if(self.music in self.game.musics):
            self.game.musics.remove(self.music)






class Sound:
    def __init__(self,src,pitch = 1,pan =.5,volume = 100):
        self.sound = pr.load_sound(f'{cur_dir}{src}')
        pr.set_sound_pitch(self.sound,pitch)
        pr.set_sound_volume(self.sound,volume/100)
        pr.set_sound_pan(self.sound,pan)
    def play(self):
        pr.play_sound(self.sound)
    def stop(self):
        pr.stop_sound(self.sound)
    def set_pitch(self,pitch):
        pr.set_sound_pitch(self.sound,pitch)
    def set_volume(self,volume):
        pr.set_sound_volume(self.sound,volume/100)
    def set_pan(self,pan):
        pr.set_sound_pan(self.sound,pan)

def instance_sound(src,pitch = 1,pan =.5,volume = 100):
    sound = pr.load_sound(f'{cur_dir}{src}')
    pr.set_sound_pitch(sound,pitch)
    pr.set_sound_volume(sound,volume/100)
    pr.set_sound_pan(sound,pan)
    if(pr.is_sound_ready(sound)):
     pr.play_sound(sound)
    

