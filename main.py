"""
Main.py

The main file for the game
"""

import sys
import helpers.gui, helpers.data, helpers.market, helpers.auxfn
import helpers.gload, helpers.gsave

def game():
    """Starts the game"""
    pass

def new_game():
    """Creates a new game instance"""
    pass

def load_game():
    """Loads a game"""
    pass

def settings():
    """Sets game settings"""
    pass

def main():
    """Main entry point"""

    menu_choice = -1
    while (menu_choice != 0):
        menu_choice = helpers.auxfn.get_user_choice(helpers.gui.main_menu(), "int")

        if (menu_choice == 1):
            game()
            menu_choice = -1
        elif (menu_choice == 2):
            #new_game()
            menu_choice = -1
        elif (menu_choice == 3):
            #load_game()
            menu_choice = -1
        elif (menu_choice == 4):
            #settings()
            menu_choice = -1
        else:
            pass

if __name__ == "__main__":
    sys.exit(main())
