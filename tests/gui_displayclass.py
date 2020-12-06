"""
gui_displayclass.py

To test whether the functions inside gui works
Note: This is not an actual test implementation
"""

from context import src
from src import gui

disp = gui.Display(displayHeight=(3*3),displayWidth=(3*5))
print(disp.display_buffer)