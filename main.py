"""
Main.py

The main entry point for the game
"""

import sys
import src.auxfn as AUXFN
import src.gui as GUI
import src.game as GAME
import src.market as MARKET

def start_game_loop(Game: object):
    """
    The main game loop.

    Args:
        * Game (`object`): The Game object as declared in main.start()

    Returns:
        * None
    """

    print("Game started")
    pass

def start():
    """
    Shows the start game menu and starts the game if a game state is loaded.

    Args:
        * None

    Returns:
        * None
    """

    # Create a Game Object
    Game = GAME.Game()
    
    def determine_menu_choice():
        if (Game.get_start_flag() == True):
            return 0
        else:
            return  -1

    menu_choice = -1
    while (menu_choice != 0):
        menu_choice = AUXFN.get_user_choice(displayText=GUI.start_menu(), returnType="int")
        if (menu_choice == 1):
            Game.create_new_game()
            menu_choice = determine_menu_choice()
        elif (menu_choice == 2):
            Game.load_game()
            menu_choice = determine_menu_choice()
        elif (menu_choice == 3):
            Game.save_game()
            menu_choice = determine_menu_choice()
        else:
            pass
    
    # Start the game loop
    if (Game.get_start_flag() == True):
        start_game_loop(Game=Game)
    
    return

def main():
    """
    Main entry point for the program
    """

    menu_choice = -1
    while (menu_choice != 0):
        menu_choice = AUXFN.get_user_choice(displayText=GUI.main_menu(), returnType="int")

        if (menu_choice == 1):
            # Start game
            start()
            menu_choice = -1
        elif (menu_choice == 2):
            # Settings
            AUXFN.settings()
            menu_choice = -1
        else:
            pass

    return

if __name__ == "__main__":
    sys.exit(main())