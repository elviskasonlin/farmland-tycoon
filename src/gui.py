"""
gui.py

Helper functions for displaying the user interface
"""

class Display(object):
    """
    docstring
    """

    display_height = 0
    display_width = 0
    display_buffer = None

    def __init__(self, displayHeight, displayWidth):
        self.display_height = displayHeight
        self.display_width = displayWidth
        self.display_buffer = [[""] * self.display_height for i in range(self.display_height)]

    def show(self):
        """
        Displays the user-interface on a 64x64 grid
        """
        print(self.display_buffer)
        pass
    
    def update(self, *args):
        """
        Updates the data
        """
        pass

    def show_help(self):
        """
        Shows help
        """
        pass

def main_menu():
    """
    Main menu with 
    """
    
    output = """
    Main Menu
    ---------
    [1] Start\n
    [2] Create New Game\n
    [3] Load Game\n
    [4] Settings\n
    [0] Quit\n

    Enter your choice: 
    """

    return output

