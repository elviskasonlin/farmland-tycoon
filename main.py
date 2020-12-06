"""
Main.py

The main file for the game
"""

import sys
import src.auxfn as AUXFN
import src.gui as GUI
import src.game as GAME
import src.market as MARKET
import src.save as SAVE

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
        menu_choice = AUXFN.get_user_choice(GUI.main_menu(), "int")

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
            settings()
            menu_choice = -1
        else:
            pass

if __name__ == "__main__":
    sys.exit(main())