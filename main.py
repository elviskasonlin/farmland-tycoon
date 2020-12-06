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
    print("game() called. Game has started.")
    pass

def new_game():
    """Creates a new game instance"""
    print("new_game() called. New game has been created.")
    pass

def load_game():
    """Loads a game"""
    print("load_game() called")
    file_name = input("Enter the file name of your save: ")
    
    save_data = SAVE.load_game(fileName=file_name)
    print(save_data)

def save_game():
    """DEBUG ONLY. Saves game"""
    print("save_game() called")
    file_name = input("Enter a name for your save: ")
    SAVE.save_game(fileName=file_name, gameState={"Key": "Value"})

def settings():
    """Sets game settings"""
    print("settings() called. Settings to be set.")
    pass

def main():
    """Main entry point"""

    menu_choice = -1
    while (menu_choice != 0):
        menu_choice = AUXFN.get_user_choice(displayText=GUI.main_menu(), returnType="int")

        if (menu_choice == 1):
            game()
            menu_choice = -1
        elif (menu_choice == 2):
            new_game()
            menu_choice = -1
        elif (menu_choice == 3):
            load_game()
            menu_choice = -1
        elif (menu_choice == 4):
            settings()
            menu_choice = -1
        elif (menu_choice == 5):
            save_game()
            menu_choice = -1
        else:
            pass

if __name__ == "__main__":
    sys.exit(main())