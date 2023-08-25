from orochi.game import Game
from orochi.graphics import *

game = Game(500,500,"Orochi installer",window_icon = load_image("src/icon.png"))
game.init()

"""
Import modules after game.init()
Example below:
"""
from orochi.community import * 
from orochi.keyboard import *
from orochi.gui import *
from orochi.files import *
from orochi.web import *
from orochi.os import *
from orochi.audio import *
from orochi.physics import *
from orochi.animation import*
from orochi.database import*
from orochi.websocket import *
from orochi.map import *
import os
import sys
folder = ""
database = Database("mydatabase")

def install(thread,game):
    global folder
    thread.store(clone_git_repo("https://github.com/slicas/Orochi-Engine",folder))
    
install_thread = Thread(game,install)
font = load_font("/src/font.ttf")

def path_install():
    global folder
    new_folder_path = folder
    current_path = os.environ["PATH"]
    new_path = new_folder_path + ";" + current_path
    os.system(f'setx PATH "{new_path}"')
    open_url("https://github.com/slicas/Orochi-Engine/wiki/Welcome")

theme = Theme(font,(0,255,0,255),(0,255,0,255))
data = [
    "","l1","","b1","",
    "","l2","","","",
    "","b2","","img","",
    "","l3","","","",
    "","","","","",
        
        
]
install_button = Button(game,theme,-60,0,"Install",64,32,12,outlined = True)
path_button = Button(game,theme,0,0,"Choose",64,32,12,outlined = True)
install_button.disabled = True
path_label = Label(game,theme,-50,0,"Install path: ",10,origin = (0,.5),align = "left")
status_label = Label(game,theme,-50,0,"",10,origin = (0,.5),align = "left")
orochi_image = Image(game,theme,0,0,load_texture("/src/icon.png"),64,64,origin = (.5,.5))
installing = False


rules = [
    ["l1",Label(game,theme,0,0,"Choose your install path",16)],
    ['b1',path_button],
    ['b2',install_button],
    ["l2",path_label],
    ['l3',status_label],
    ['img',orochi_image]
    ]
screen = GuiMap(data,rules,500/5,5,5)
screen.init()
screen.show_all()
finished = False

def game_update():
    global install_button,folder,installing,status_label,install_thread,finished
    orochi_image.angle += 1
    
    path_label.text = f"Install path: {folder}"
    if(path_button.is_pressed()):
        folder = get_folder()
        folder += "\\orochi\\"
    if(folder != "" and not installing):
        install_button.disabled = False
    if(install_button.is_pressed()):
        install_thread.execute()
        installing = True
        status_label.text = "Installing..."
    if(len(install_thread.values) > 0 and not finished):
        if(install_thread.values[0] == True):
            status_label.text = "Done!"
            path_install()
            open_url("https://github.com/slicas/Orochi-Engine/wiki/Welcome")
            finished = True
        else:
            status_label.text = "Error!"
            
    game.clear_color = (0,0,0,255)
    
    
    
game.set_update(game_update)


while game.running:
    game.looping()




"""

Special thanks to:
Raylib: https://github.com/raysan5/raylib
Lapce: https://github.com/lapce/lapce
Pygame: https://github.com/pygame/pygame
Pixelorama: https://github.com/Orama-Interactive/Pixelorama

"""