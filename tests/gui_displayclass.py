"""
gui_displayclass.py

To test whether the functions inside gui works
Note: This is not an actual test implementation
"""

from context import src
from src import gui

disp = gui.Board(boardHeight=(3*3),boardWidth=(3*5))
disp.show_board()
print(disp.get_board_height())
print(disp.get_board_width())