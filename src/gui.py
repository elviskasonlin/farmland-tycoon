"""
gui.py

Helper items for displaying UI elements
"""

# Board Object
class Board(object):
    """
    docstring
    """

    board_height = 0
    board_width = 0
    display_buffer = None

    def __init__(self, boardHeight, boardWidth):
        self.board_height = boardHeight
        self.board_width = boardWidth
        self.display_buffer = [[""] * self.board_width for i in range(self.board_height)]

    def get_board_height(self):
        """
        Returns the set board_height

        Returns:
            * board_height (`int`)
        """
        return self.board_height

    def get_board_width(self):
        """
        Returns the set board_width

        Returns:
            * board_width (`int`)
        """
        return self.board_width

    def show_board(self):
        """
        Displays the board with its current state
        """
        # For debugging
        print(self.display_buffer)
        return None
    
    def update_board(self, *args):
        """
        Updates the data
        """
        pass

# The string for main menu
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

