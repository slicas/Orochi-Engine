from orochi.layer import Layer
class Scene:
    def __init__(self,ID,game,width,height,persistent = True):
        self.__ID = ID
        self.game = game
        self.width = width
        self.height = height
        self.layers = [Layer("0"),Layer("GUI")]
        self.objects = []
        self.persistent = persistent
        self.game.scenes.append(self)
        self.__on_ready = None
    def get_id(self):
        return self.__ID
    def add_layer(self,layer : object):
        self.layers.append(layer)
    def set_on_ready(self,function):
        self.__on_ready = function
    def get_on_ready(self):
        if(self.__on_ready != None):
            return self.__on_ready(self,self.game)