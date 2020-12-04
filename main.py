"""
Main.py

The main file for the game
"""

import sys
import src.gui, src.game, src.market, src.auxfn, src.save

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
        menu_choice = src.auxfn.get_user_choice(src.gui.main_menu(), "int")

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