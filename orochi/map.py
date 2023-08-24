import PIL
import random
from orochi.object import object_instantiate,instance_model

CHAR = "CHAR"
NOISE = "NOISE"
HEX = "HEX"
def get_map_from_image(image_path):
        def rgb_to_hex(rgb):
            return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
        img = PIL.Image.open(image_path)
        img = img.convert('RGB')
        pixels = img.load() 
        width, height = img.size
        map = []
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]
                hex_color = rgb_to_hex(pixel)
                map.append(hex_color)

        return map
class Map():
    def __init__(self,type,data,rules,cell_size,rows,columns):
        self.__type = type
        if(type == "HEX"):
            self.__data = get_map_from_image(f'{self.game.cur_dir}{data}')
        self.__data = data
        self.__rules = rules
        self.__cell_size = cell_size
        self.__rows = rows
        self.__columns = columns
        self.__width = cell_size*self.__columns
        self.__height = cell_size*self.__rows
        self.__objects = []
    def get_objects(self):
        return self.__objects
    def init(self,scene,x = 0,y = 0,repeat_x = 1,repeat_y = 1,sep_x = 0,sep_y = 0):
        def inst(rule,repeat_y,repeat_x):
                params = rule[1]
                e = object_instantiate(params['game'],scene,params['layer'],((self.__width + sep_x)*repeat_x)+(x + (self.__cell_size*c)),((self.__height + sep_y)*repeat_y) + (y + (self.__cell_size*r)),params['width'],params['height'],params['image'],params['tags'],params['origin'],params['tint'],params['angle'],params['update'],params['draw'])
                self.__objects.append(e)
        for yy in range(repeat_y):
            for xx in range(repeat_x):
                if(self.__type != "NOISE"):
                    r = 0
                    c = -1
                    for cell in self.__data:
                        if(r <= self.__rows):
                            if(c < self.__columns-1):
                                c += 1
                            else: 
                                c = 0
                                r += 1
                            for rule in self.__rules:
                                if(self.__type == "HEX"):
                                    if(rule[0].upper() == cell.upper()):
                                        inst(rule,yy,xx)
                                elif(self.__type == "CHAR"):
                                    if(str(rule[0]) == str(cell)):
                                        inst(rule,yy,xx)
                                        
                else:
                    r = 0
                    c = -1
                    for cell in self.__data:
                        if(r <= self.__rows):
                            if(c < self.__columns-1):
                                c += 1
                            else: 
                                c = 0
                                r += 1


                            for rule in self.__rules:
                                if(cell >= rule[0][0][0] and cell <= rule[0][1][0]):
                                    if(cell == rule[0][0][0] and rule[0][0][1] == True):
                                        inst(rule,yy,xx)
                                        continue
                                    elif(cell == rule[0][0][0] and rule[0][0][1] == False):
                                        continue
                                    elif(cell == rule[0][1][0] and rule[0][1][1] == True):
                                        inst(rule,yy,xx)
                                        continue
                                    elif(cell == rule[0][1][0] and rule[0][1][1] == False):
                                        continue
                                    else:
                                        inst(rule,yy,xx)
                                        continue
        return True

            
