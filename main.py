"""
Main.py

The main entry point for the game
"""

import sys
import src.auxfn as AUXFN
import src.gui as GUI
import src.game as GAME
import src.market as MARKET

def start():
    """
    Contains the core game loop. Shows the start game menu and starts the game if a game state is loaded.

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
            # For testing only. Will be removed later
            Game.save_game()
            menu_choice = determine_menu_choice()
        else:
            pass
    
    # Start the game loop
    if (Game.get_start_flag() == True):
        
        while (Game.get_game_ended_flag() != True):
            user_command = AUXFN.get_user_choice(displayText="Cmd input: ", returnType="str")
            print(user_command)
            pass
    
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