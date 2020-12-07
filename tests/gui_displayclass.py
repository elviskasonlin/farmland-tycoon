"""
gui_displayclass.py

To test whether the functions inside gui works
Note: This is not an actual test implementation
"""

from context import src
from src import gui

"""
disp = gui.Board(boardHeight=(3*3),boardWidth=(3*5))
disp.show_board()
print(disp.get_board_height())
print(disp.get_board_width())
"""

print(gui.longest_width("""
    {0}`plots`: Shows the game board{1}\n
    \t Example: `plots`
    {0}`plant <X,Y> <TYPE>`: Plants a plant of a given <type> at specified <X,Y> coordinates{1}\n
    \t Example: `plant 1,1 corn`\n
    {0}`harvest <XY>`: Harvests a plant at specified <X,Y> coordinates{1}\n
    \t Example: `harvest 1,1`\n
    {0}`upgrade <TYPE>`: Buys an upgrade.{1}\n
    \t Available upgrades: (plot yield upgrade: "land"),\n
    \t                     (productivity upgrades: "cow", "machinery", "automation", "labour")\n
    \t Example: `upgrade land`\n
    {0}`warehouse`: Shows items and their quantity in the warehouse{1}\n
    \t Example: `warehouse`\n
    {0}`sell <ITEM> <QTY>`: Sells items in the warehouse{1}\n
    \t Example: `sell apple 5`\n
    {0}`save`: Ends your turn{1}\n
    {0}`exit`: Saves the game{1}\n
    """))