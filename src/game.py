"""
game.py

The game class. Has functions related to the functioning of the game itself.
"""

import copy
from . import saves as SAVES

class Game(object):
    """
    Main game class
    """

    # Variables
    game_state = { "days": 0, }
    start_game = False

    def __init__(self):
        pass

    # Getters
    def get_game_state(self):
        return self.game_state
    
    def get_start_flag(self):
        return self.start_game

    # Setters
    def set_game_state(self, gameState: dict):
        """
        Sets the game state with given gamestate parameter. Used for loading data from save files.

        Args:
            * gameState (`dict`): The game state as a dictionary

        Returns:
            * None
        """
        self.game_state = copy.deepcopy(gameState)
        return

    def create_new_game(self):
        """
        Prepares the initial game state for the new game

        Args:
            * None

        Returns:
            * None
        """

        print("create_new_game called!")
        self.start_game = True
        return

    def load_game(self):
        """
        Loads a game from an external save file in .json format

        Args:
            * None

        Returns:
            * None
        """

        file_name = input("Enter the file name of your save: ")
        operation_flag, data = SAVES.load_game(fileName=file_name)

        if (operation_flag == 1):
            self.set_game_state(gameState=data)
            print("Game has been loaded from {}".format(file_name))
            self.start_game = True
        else:
            print(data + "\nTry loading your save file again.")
            self.start_game = False
        
        return

    def save_game(self):
        """
        Saves the game to an external save file in .json format

        Args:
            * None

        Returns:
            * None
        """

        file_name = input("Enter a name for your save: ")
        operation_flag, data = SAVES.save_game(fileName=file_name, gameState=self.game_state)

        if (operation_flag == 1):
            print(data)
            self.start_game = True
        else:
            print(data)
            self.start_game = False

        return