import pyray as pr
from orochi.mouse import *
from orochi.collision import *
from orochi.graphics import *
from orochi.keyboard import *
import time
from orochi.os import *
import keyboard
def get_text(thread,game):
    thread.store("")
    notlisten = ["right shift","left shift","alt gr","alt","tab"]
    while game.running:
        if(thread.active):
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if thread.active and event.name == "backspace":
                    thread.values[0] = thread.values[0][:-1]
                elif thread.active and thread.profile.input.max_len > len(thread.values[0]) and event.name == "space":
                    thread.values[0] += " "
                else:
                    if(event.name not in notlisten and thread.active and thread.profile.input.max_len > len(thread.values[0])):
                        thread.values[0] += event.name
        else:
            time.sleep(0.2)

class GuiMap:
    def __init__(self,data,rules,cell_size,rows,columns):
        self.__data = data
        self.__rules = rules
        self.__cell_size = cell_size
        self.__rows = rows
        self.__columns = columns
        self.__width = cell_size*self.__columns
        self.__height = cell_size*self.__rows
        self.__gui_components= []
    def get_gui_components(self):
        return self.__gui_components
    def init(self,x = 0,y = 0,repeat_x = 1,repeat_y = 1,sep_x = 0,sep_y = 0):
        def inst(rule,repeat_y,repeat_x):
                gui = rule[1]
                shift_x = gui.x
                shift_y = gui.y
                origin = gui.origin
                gui.x = ((((self.__width + sep_x)*repeat_x)+(x + (self.__cell_size*c))) + (self.__cell_size*origin[0])) + shift_x
                gui.y = (((self.__height + sep_y)*repeat_y) + (y + (self.__cell_size*r))+ (self.__cell_size*origin[1])) + shift_y
                self.__gui_components.append(gui)
        for yy in range(repeat_y):
            for xx in range(repeat_x):
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
                                if(rule[0].upper() == cell.upper()):
                                    inst(rule,yy,xx)
        return True
    def show_all(self):
        for component in self.__gui_components:
            component.show()
    def hidden_all(self):
        for component in self.__gui_components:
            component.hidden()  


class Theme:
    def __init__(self,font,primary_color,secoundary_color):
        self.font = font
        self.primary_color = primary_color
        self.secoundary_color = secoundary_color
class GuiComponent:
    def __init__(self,game,theme : Theme,x,y):
        self.game = game
        self.theme = theme
        self.x = x
        self.y = y
        self._visible = False
    def show(self):
        if(not self in self.game.gui_components):
            self.game.gui_components.append(self)
            self._visible = True

    def hidden(self):
        if(self in self.game.gui_components):
            self.game.gui_components.remove(self)
            self._visible = False

class Input(GuiComponent):
    def __init__(self,game,theme,x,y,width,font_size,origin = (.5,.5),line_size = 1,max_len = 0):
        super().__init__(game,theme,x,y)
        self.font_size = font_size
        self.value =  ""
        self.width = width
        self.origin = origin
        self.line_size = line_size
        self.active = False
        self.disabled = False
        self.max_len = 9999999999 if max_len == 0 else max_len
        self.input_thread = Thread(self.game,get_text)
        self.input_thread.profile.input = self
        len
    def show(self):
        self.input_thread.execute()
        return super().show()
    def hidden(self):
        self.active = False
        return super().hidden()
    def mouse_enter(self):
        if(self._visible):
            return rect_collision(pr.Rectangle(self.x - (self.width*self.origin[0]),(self.y) - (self.line_size*self.origin[1]),self.width,self.line_size),pr.Rectangle(get_gui_mouse_x(),get_gui_mouse_y(),5,20))
    def is_pressed(self):
            if(self._visible):
                if(self.mouse_enter() and is_mouse_button_pressed(MB_LEFT) and not self.disabled):
                    return True
                else:
                    return False
    def is_down(self):
        if(self._visible):
            if(self.mouse_enter() and is_mouse_button_down(MB_LEFT) and not self.disabled):
                return True
            else:
                return False
    def render(self):
        pr.draw_line_ex(pr.Vector2((self.x - (self.width*self.origin[0])),(self.y - (self.line_size*self.origin[1]))),pr.Vector2((self.x - (self.width*self.origin[0])) + self.width,(self.y - (self.line_size*self.origin[1]))),self.line_size,self.theme.primary_color)
        draw_text(self.theme.font,self.value,self.x - (self.width*self.origin[0]),self.y - 15,(0,0),0,self.font_size,1,self.theme.secoundary_color,align = "right")

        pass
    def update(self):
        self.input_thread.active = self.active
        if(self.active):
            change_cursor(INPUT_CURSOR)
        if(len(self.input_thread.values) > 0):
            self.value = self.input_thread.values[0]
        if(self.mouse_enter()):
            if(not self.active):
                change_cursor(POINTER_CURSOR)
        else:
            if(is_mouse_button_pressed(MB_LEFT)):
                self.active = False
        if(self.is_pressed()):
            self.active = not self.active
        


class Label(GuiComponent):
    def __init__(self,game,theme,x,y,text,font_size,origin = (.5,.5),align = "center"):
        super().__init__(game,theme,x,y)
        self.text = text
        self.font_size = font_size
        self.theme = theme
        self.text_color = self.theme.secoundary_color
        self.size = pr.measure_text_ex(self.theme.font,self.text,self.font_size,1)
        self.origin = origin
        self.align = align
    def show(self):
        return super().show()
    def hidden(self):
        return super().hidden()
    
    def render(self):
        draw_text(self.theme.font,self.text,self.x,self.y,(self.origin[0],self.origin[1]),0,self.font_size,1,self.text_color,align = self.align)

    def mouse_enter(self):
        if(self._visible):
            return rect_collision(pr.Rectangle(self.x - (self.size.x*self.origin[0]),self.y- (self.size.y*self.origin[1]),self.size.x,self.size.y),pr.Rectangle(get_gui_mouse_x(),get_gui_mouse_y(),1,1))
    
    def is_pressed(self):
            if(self._visible):
                if(self.mouse_enter() and is_mouse_button_pressed(MB_LEFT) and not self.disabled):
                    return True
                else:
                    return False
    def is_down(self):
        if(self._visible):
            if(self.mouse_enter() and is_mouse_button_down(MB_LEFT) and not self.disabled):
                return True
            else:
                return False
    def highlight(self):
        self.text_color = self.theme.primary_color
    def update(self):
        self.text_color = self.theme.secoundary_color
        self.size = pr.measure_text_ex(self.theme.font,self.text,self.font_size,1)
        pass
   

class Button(GuiComponent):
    def __init__(self,game,theme,x,y,text,width,height,font_size,outlined = False,rounded = False,origin = (.5,.5)):
        super().__init__(game,theme,x,y)
        self.init_width = width
        self.init_height = height
        self.width = width
        self.height = height
        self.init_font_size = font_size
        self.font_size = font_size
        self.text = text
        self.theme = theme
        self.rounded =rounded
        self.outlined = outlined
        self.bg_color = self.theme.primary_color
        self.font_color = self.theme.secoundary_color
        self.disabled = False
        self.origin = origin
    
    def show(self):
        return super().show()
    def hidden(self):
        return super().hidden()
    
    def render(self):
        if(not self.outlined and not self.rounded):
            pr.draw_rectangle_pro(pr.Rectangle(self.x,self.y,self.width,self.height),(self.width*self.origin[0],self.height*self.origin[1]),0,self.bg_color)
        elif(self.outlined and not self.rounded):
            pr.draw_rectangle_lines(int(self.x - (self.width*self.origin[0])),int(self.y - (self.height*self.origin[1])),self.width,self.height,self.bg_color)
        elif(self.outlined and self.rounded):
            pr.draw_rectangle_rounded_lines(pr.Rectangle(int(self.x - (self.width*self.origin[0])),int(self.y - (self.height*self.origin[1])),self.width,self.height),.5,1,1,self.bg_color)
        elif(self.rounded):
            pr.draw_rectangle_rounded(pr.Rectangle(int(self.x - (self.width*self.origin[0])),int(self.y - (self.height*self.origin[1])),self.width,self.height),.5,1,self.bg_color)

        draw_text(self.theme.font,self.text,self.x,self.y,(self.origin[0],self.origin[1]),0,self.font_size,1,self.font_color)

    def mouse_enter(self):
        if(self._visible):
            return rect_collision(pr.Rectangle(self.x - (self.init_width*self.origin[0]),self.y- (self.init_height*self.origin[1]),self.init_width,self.init_height),pr.Rectangle(get_gui_mouse_x(),get_gui_mouse_y(),1,1))
    def is_pressed(self):
        if(self._visible):
            if(self.mouse_enter() and is_mouse_button_pressed(MB_LEFT) and not self.disabled):
                return True
            else:
                return False
    def is_down(self):
        if(self._visible):
            if(self.mouse_enter() and is_mouse_button_down(MB_LEFT) and not self.disabled):
                return True
            else:
                return False
    def update(self):
        if(not self.disabled):
            if(self.mouse_enter()):
                change_cursor(POINTER_CURSOR)
                self.bg_color = self.theme.secoundary_color
                self.font_color = self.theme.primary_color
            else:
                self.bg_color = self.theme.primary_color
                self.font_color = self.theme.secoundary_color
            if(self.is_down()):
                self.font_size = int(self.init_font_size * .8)
                self.width = int(self.init_width * .8)
                self.height = int(self.init_height * .8)
            else:
                self.font_size = self.init_font_size
                self.width = self.init_width 
                self.height = self.init_height

