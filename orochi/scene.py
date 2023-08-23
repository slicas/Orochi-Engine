from orochi.layer import Layer
class Scene:
    def __init__(self,ID,game,width,height):
        self.__ID = ID
        self.game = game
        self.width = width
        self.height = height
        self.layers = [Layer("0"),Layer("GUI")]
        self.objects = []
        self.game.scenes.append(self)
    def get_id(self):
        return self.__ID
    def add_layer(self,layer : object):
        self.layers.append(layer)
