"""
gui.py

Helper items for displaying UI elements
"""

# Text formatting
# Yanked from https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
class TypeFormat:
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

def create_separator(char: str, length: int, includeNewLine: bool):
    output = None
    if (includeNewLine == True):
        output = "\n" + (char * length) + "\n"
    else:
        output = char * length
    return output

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
        * (`str`): Start menu as an F-String
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
        * (`str`): Settings menu as an F-String
    """

    output = """
    Settings
    --------
    Nil\n
    """
    return output

def get_help_menu():
    """
    The text for help menu during the game loop

    Returns:
        * (`str`): Help menu as an F-String
    """
    
    body = """
    Available commands:

    {0}`plots`:{1}
    \t {2}Shows the game board{1}\n
    \t Example: `plots`\n
    {0}`plant <X,Y> <CROP NAME>`:{1}
    \t {2}Plants a crop of a given <CROP NAME> at specified <X,Y> coordinates.
    \t Type `crops` to see a list of available crops and their attributes.{1}\n
    \t Example: `plant 1,1 corn`\n
    {0}`harvest <X,Y>`:{1}
    \t {2}Harvests a crop at specified <X,Y> coordinates{1}\n
    \t Example: `harvest 1,1`\n
    {0}`upgrade <UPGRADE NAME>`:{1}
    \t {2}Buys an upgrade of a given <UPGRADE NAME>.
    \t Type `upgrades` to see a list of available upgrades and their attributes.{1}\n
    \t Available types: Plot yield or Productivity upgrade
    \t Example: `upgrade land`\n
    {0}`purchased`:{1}
    \t {2}Shows purchased upgrades{1}\n
    \t Example: `purchased`\n
    {0}`warehouse`:{1}
    \t {2}Shows items and their quantity in the warehouse{1}\n
    \t Example: `warehouse`\n
    {0}`sell <ITEM> <QTY>`:{1}
    \t {2}Sells items in the warehouse{1}\n
    \t Example: `sell apple 5`\n
    {0}`save`: {2}Ends your turn{1}{1}\n
    {0}`exit`: {2}Saves the game{1}{1}\n
    """.format(TypeFormat.BOLD,TypeFormat.END,TypeFormat.PURPLE)

    title = "{0}HELP MENU{1}".format(TypeFormat.BOLD, TypeFormat.END).center(get_longest_width(text=body))
    
    line_separator = create_separator(char="-", length=get_longest_width(text=body), includeNewLine=True)

    output = line_separator + title + line_separator + body

    return output

def print_beautified_dictionary(dictionary: dict):
    """
    Returns a beautified dictionary ready for printing to console

    Args:
        dictionary (`dict`): The dictionary items to beautify

    Returns:
        (`str`): Beautified dictionary as a string
    """
    output = ""
    for item, value in dictionary.items():
        output = output.join(str(item) + ": " + str(value) + "\n")
    return output