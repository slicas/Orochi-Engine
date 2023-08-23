class TagStore:
    def __init__(self):
        self.tags = []

tag_store = TagStore()

class Tag:
    def __init__(self,name):
        self.__name = name
        self.objects  = []
        self.__store = tag_store
        self.__store.tags.append(self)
    def get_name(self):
        return self.__name
    def get_objects(self):
        return self.objects
    def add(self,entitie):
        entitie.tags.append(self)
        self.objects.append(entitie)
    def delete(self,entitie):
        self.objects.remove(entitie)

