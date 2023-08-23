from orochi.game import Game

game = Game(500,500)
game.init()

"""
Import modules after game.init()
Example below:
"""
from orochi.utils import * 


def game_update():
    pass
game.set_update(game_update)


while game.running:
    game.looping()




"""

Special thanks to:
Raylib: https://github.com/raysan5/raylib
Lapce: https://github.com/lapce/lapce
Pygame: https://github.com/pygame/pygame

"""