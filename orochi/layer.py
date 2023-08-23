
def get_layer_by_id(scene,ID):
    for layer in scene.layers:
        if(layer.get_id() == ID):
            return layer

class Layer:
    def __init__(self,ID):
        self.__ID = ID
        self.__objects = []
        self.__particles = []
    def get_id(self):
        return self.__ID
    def get_objects(self):
        return self.__objects
    def get_particles(self):
        return self.__particles
    def add_particle(self,particle):
        self.__particles.append(particle)
    def delete_particle(self,particle):
        self.__particles.remove(particle)
    def add(self,object):
        self.__objects.append(object)
    def delete(self,object):
        self.__objects.remove(object)

