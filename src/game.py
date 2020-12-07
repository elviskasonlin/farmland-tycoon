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
    game_state = { "days": 0, "climate": None, "land": {"size": None, "plots": None}, "upgrades": {"land": 0, "equipment": {"cows": 0, "machinery": 0, "automation": 0}, "labour": 1}, "money": 0, "productivity": None, "maintenance": None }
    game_ended_flag = False
    start_game_flag = False

    def __init__(self):
        pass

    # GETTERS
    def get_game_state(self):
        return self.game_state
    
    def get_start_flag(self):
        return self.start_game_flag

    def get_game_ended_flag(self):
        return self.game_ended_flag

    def can_player_afford(self, cost: float):
        return self.game_state["money"] >= cost

    def get_player_upgrades(self):
        """
        Gets player's current upgrades and returns it as a tuple

        Returns:
            (`tuple`): land_tier, equipment_cows_count, equipment_machinery_count, equipment_automation_count, labour_count
        """

        upgrades = self.game_state["upgrades"]
        equipment = upgrades["equipment"]

        land_tier = upgrades["land"]
        equipment_cows_count = equipment["cows"]
        equipment_machinery_count = equipment["machinery"]
        equipment_automation_count = equipment["automation"]
        labour_count = upgrades["labour"]

        to_return = (land_tier, equipment_cows_count, equipment_machinery_count, equipment_automation_count, labour_count)
        return to_return
    
    def get_land_size(self):
        """Gets the land size

        Returns:
            (`tuple`): (Plots in x-axis, Plots in y-axis)
        """
        return self.game_state["land"]["size"]

    # SETTERS
    def set_land_size(self, xCount: int, yCount: int):
        """
        Sets the number of plots in x and y directions

        Args:
            xCount (int): No. of plots in x axis
            yCount (int): No. of plots in y axis
        """
        self.game_state["land"]["size"] = (xCount, yCount)
        return

    def set_game_state(self, gameState: dict):
        """
        Sets the game state with given gamestate parameter. Used for loading data from save files.

        Args:
            gameState (`dict`): The game state as a dictionary
        """
        self.game_state = copy.deepcopy(gameState)
        return

    # ---------------------
    # Create/Load/Save Game
    # ---------------------

    def create_new_game(self):
        """
        Prepares the initial game state for the new game
        """

        print("create_new_game called!")

        self.set_land_size(xCount=3,yCount=3)

        self.start_game_flag = True
        return

    def load_game(self):
        """
        Loads a game from an external save file in .json format
        """

        file_name = input("Enter the file name of your save: ")
        operation_flag, data = SAVES.load_game(fileName=file_name)

        if (operation_flag == 1):
            self.set_game_state(gameState=data)
            print("Game has been loaded from {}".format(file_name))
            self.start_game_flag = True
        else:
            print(data + "\nTry loading your save file again.")
            self.start_game_flag = False
        
        return

    def save_game(self):
        """
        Saves the game to an external save file in .json format
        """

        file_name = input("Enter a name for your save: ")
        operation_flag, data = SAVES.save_game(fileName=file_name, gameState=self.get_game_state())

        if (operation_flag == 1):
            print(data)
            #self.start_game_flag = True
        else:
            print(data)
            #self.start_game_flag = False

        return