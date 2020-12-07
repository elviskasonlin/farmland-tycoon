from context import src
from src import game as GAME

Game = GAME.Game()
Game.set_land_size(xCount=3,yCount=3)
Game.create_board()
print(Game.get_board())