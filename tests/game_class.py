"""
game_class.py

To test whether the functions inside gui works
Note: This is not an actual test implementation
"""

from context import src
from src import game as GAME

game = GAME.Game()
game.set_land_size(xCount=3,yCount=5)
print(game.get_land_size())