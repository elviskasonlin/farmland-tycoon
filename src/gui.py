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

    # Getters
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

    # Setters    
    def update_board(self, *args):
        """
        Updates the data
        """
        pass

# The string for main menu
def main_menu():
    """
    The main menu (upon start) 
    """
    
    output = """
    Main Menu
    ---------
    [1] Start\n
    [2] Settings\n
    [0] Quit\n

    Enter your choice: 
    """

    return output

def start_menu():
    """
    The main menu (upon start) 
    """
    
    output = """
    Start
    -----
    [1] New Game\n
    [2] Load Game\n
    [0] Back\n

    Enter your choice: 
    """

    return output

def settings_menu():
    """
    Settings menu
    """

    output = """
    Settings
    --------
    Nil\n
    """
    return output

def game_menu():
    """
    The game menu during gameplay
    """

    output = """
    Game Menu
    ---------
    Nil\n
    """
    return output

def help_menu():
    """
    Shows the help menu
    """

    output = """
    Help Menu
    ---------
    Nil\n
    """
    return output

def upgrades_menu():
    """
    Shows the upgrades menu
    """

    output = """
    Help Menu
    ---------
    Nil\n
    """
    return output