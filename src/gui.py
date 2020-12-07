"""
gui.py

Helper items for displaying UI elements
"""

# Text formatting
# Yanked from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Find longest width from a string
def get_longest_width(text: str):
  lines = text.split('\n')
  width = max(map(len, lines))
  return width

# Board Object
class Board(object):
    """
    Board class for board operations
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
def get_main_menu():
    """
    The text for main menu
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

def get_start_menu():
    """
    The text for start menu entered from the main menu

    Returns:
        (`str`): Start menu as an F-String
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

def get_settings_menu():
    """
    The text for settings menu entered from the main menu

    Returns:
        (`str`): Settings menu as an F-String
    """

    output = """
    Settings
    --------
    Nil\n
    """
    return output

def get_game_menu():
    """
    The text for game menu during the game loop

    Returns:
        (`str`): Game menu as an F-String
    """

    output = """
    Game Menu
    ---------
    Nil\n
    """
    return output

def get_help_menu():
    """
    The text for help menu during the game loop

    Returns:
        (`str`): Help menu as an F-String
    """
    
    body = """
    Available commands:

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
    """.format(color.BOLD,color.END)

    title = "Help Menu".center(get_longest_width(text=body))

    output = title + "\n" + ("-" * get_longest_width(text=body)) + "\n" + body

    return output

def get_upgrades_menu():
    """
    Shows the upgrades menu
    """

    output = """
    Help Menu
    ---------
    Nil\n
    """
    return output