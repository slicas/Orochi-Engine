import time
from orochi.object import Profile
class Alarm:
    def __init__(self,secounds,function = None,debug = False,debug_ID = ""):
        self.secounds = secounds
        self.function = function
        self.start_time = 0
        self.__started = False
        self.active = True
        self.store = Profile()
        self.debug = debug
        self.debug_ID = debug_ID
    def set_function(self,function):
        self.function = function
    def execute(self):
        if(not self.__started and self.active):
            self.start_time = time.time()
            self.__started = True
        if(self.active and self.__started):
            now = time.time()
            if(self.debug):
                print("------------------------------------------------------")
                print(f"Running... {self.debug_ID}\nSecounds:{self.secounds}\nStart Time: {self.start_time}\nNow: {now}\nDif: {now - self.start_time}")
            if(now - self.start_time >= self.secounds):
                if(self.function):
                    if(self.debug):
                        print("------------------------------------------------------")
                        print(f"Function {self.debug_ID} executed... {self.debug_ID}\nStart Time: {self.start_time}\nNow: {now}\nDif: {now - self.start_time} ")
                    self.function()
                    self.__started = False
    def start(self,game):
        if not self.__started:
            if(not self in game.alarms):
                game.alarms.append(self)
                self.start_time = time.time()
                self.__started = True            
        if(self.active and self.__started):
            now = time.time()
            if(self.debug):
                print("------------------------------------------------------")
                print(f"Running... {self.debug_ID}\nSecounds:{self.secounds}\nStart Time: {self.start_time}\nNow: {now}\nDif: {now - self.start_time}")
            if(now - self.start_time >= self.secounds):
                if(self.function):
                    if(self.debug):
                        print("------------------------------------------------------")
                        print(f"Function {self.debug_ID} executed... {self.debug_ID}\nStart Time: {self.start_time}\nNow: {now}\nDif: {now - self.start_time} ")
                    self.function()
                    self.__started = False
                    if(self in game.alarms):
                        game.alarms.remove(self)

    def set_time(self,secounds):
        self.secounds = secounds
    def set_function(self,function):
        self.function = function