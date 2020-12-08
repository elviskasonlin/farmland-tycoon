"""
game.py

The game class. Has functions related to the functioning of the game itself.
"""

"""
Note: Remember to use `update_board_in_gamestate` after every board operation so that the `plots` data in `game_state` is synchronised with the `game_board`
"""

import copy
from . import saves as SAVES
from . import auxfn as AUXFN

class Game(object):
    """
    Main game class
    """

    # Variables
    game_state = {
        "days": 0,
        "climate": None,
        "land": {"size": None, "plots": None},
        "upgrades": {"land": 0, "cows": 0, "machinery": 0, "automation": 0, "labour": 1},
        "money": 0,
        "productivity": None,
        "maintenance": None,
        "warehouse": {}
        }

    game_board = {}
    game_output_width = 95

    available_crops = {}
    available_upgrades = {}

    game_ended_flag = False
    start_game_flag = False

    # --------------
    # Initialisation
    # --------------

    def __init__(self):
        try:
            self.available_crops = AUXFN.load_configuration("default_crops")
            self.available_upgrades = AUXFN.load_configuration("default_upgrades")
        except Exception:
            raise Exception("Encountered error while loading configuration files.")

    # ----------
    # Core Stuff
    # ----------
    
    # +++++++
    # Core: Getters
    # +++++++

    def get_game_state(self):
        """
        Returns the game state (which is stored as a dictionary)

        Returns:
            * game_state (`dict`): The current game state as a dictionary
        """
        self.update_board_in_gamestate
        return self.game_state
    
    def get_start_flag(self):
        """
        Returns the flag for whether the game can start.

        Returns:
            * (`bool`): Flag for whether the game can start
        """
        return self.start_game_flag

    def get_game_ended_flag(self):
        """
        Returns the flag for whether the game can has ended.

        Returns:
            * (`bool`): Flag for whether the game has ended
        """
        return self.game_ended_flag

    def get_game_output_width(self):
        return self.game_output_width

    def get_player_upgrades(self):
        """
        Gets player's current upgrades and returns it as a tuple

        Returns:
            * (tuple): land_tier, equipment_cows_count, equipment_machinery_count, equipment_automation_count, labour_count
        """

        upgrades = self.game_state["upgrades"]

        land_tier = upgrades["land"]
        equipment_cows_count = upgrades["cows"]
        equipment_machinery_count = upgrades["machinery"]
        equipment_automation_count = upgrades["automation"]
        labour_count = upgrades["labour"]

        to_return = (land_tier, equipment_cows_count, equipment_machinery_count, equipment_automation_count, labour_count)
        return to_return
    
    def get_land_size(self, axis=None):
        """
        Returns the land size as a tuple by default. You may specify a specific axis to get the size at that axis.

        Args:
            * (optional) axis (str): "x", "y" axes

        Returns:
            * By default - (tuple): The number of plots in both x and y axes as follows: (x-count, y-count)
            * If axis is specified - (int): Returns the number of plots in the specified axis
        """
        land_size_as_tuple = self.game_state["land"]["size"]

        if (axis != None):
            if (axis[0].lower() == "x"):
                return land_size_as_tuple[0]
            elif (axis[0].lower() == "y"):
                return land_size_as_tuple[1]
        else:
            return land_size_as_tuple

    def get_available_crop_names(self):
        """
        Returns the names of all available crops

        Returns:
            (`list`): List with available crops
        """
        available_crops_as_list = list()
        for crop in self.available_crops:
            available_crops_as_list.append(crop)
        return available_crops_as_list

    def get_available_upgrade_names(self):
        """
        Returns the names all available upgrades

        Returns:
            (`list`): List with available upgrades
        """
        available_upgrades_as_list = list()
        for upgrade in self.available_upgrades:
            available_upgrades_as_list.append(upgrade)
        return available_upgrades_as_list

    # +++++++
    # Core: Setters
    # +++++++

    def set_game_output_width(self, width: int):
        self.game_output_width = width
        return

    def set_land_size(self, xCount: int, yCount: int):
        """
        Sets the number of plots in x and y directions

        Args:
            * xCount (int): No. of plots in x axis
            * yCount (int): No. of plots in y axis
        """
        self.game_state["land"]["size"] = (xCount, yCount)
        return

    def set_game_state(self, gameState: dict):
        """
        Sets the game state with given gamestate parameter. Used for loading data from save files.

        Args:
            * gameState (`dict`): The game state as a dictionary
        """
        self.game_state = copy.deepcopy(gameState)
        return

    # ------
    # Checks
    # ------

    def can_player_afford(self, cost):
        return self.game_state["money"] >= cost

    def is_coord_valid(self, coordX: int, coordY: int):
        """
        Checks whether a coordinate is valid

        Args:
            * coordX (`int`): x-coordinate
            * coordY (`int`): y-coordinate

        Returns:
            * (`bool`): `True` if the coordinate is valid, `False` if the coordinate is invalid
        """
        x_bounds = self.get_land_size("x") - 1
        y_bounds = self.get_land_size("y") - 1
        condition = coordX > x_bounds or coordX < 0 or coordY > y_bounds or coordY < 0
        if (condition):
            return False
        else:
            return True

    def is_plant_valid(self, plantType: str):
        if (plantType not in self.get_available_crop_names()):
            return False
        else:
            return True

    # ---------------------
    # Create/Load/Save Game
    # ---------------------

    def create_new_game(self):
        """
        Prepares the initial game state for the new game
        """

        print("create_new_game called!")

        self.set_land_size(xCount=3,yCount=3)
        self.set_game_output_width(95)
        self.create_board()

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

            self.set_board(data["land"]["plots"])
            self.update_board_in_gamestate()

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
        self.update_board_in_gamestate()

        file_name = input("Enter a name for your save: ")
        operation_flag, data = SAVES.save_game(fileName=file_name, gameState=self.get_game_state())

        if (operation_flag == 1):
            print(data)
            #self.start_game_flag = True
        else:
            print(data)
            #self.start_game_flag = False

        return

    # ------------------------
    # Board (Plots) Operations
    # ------------------------

    def update_board_in_gamestate(self):
        self.game_state["land"]["plots"] = copy.deepcopy(self.game_board)

    def create_board(self):
        self.game_board = [[""] * self.get_land_size("x") for i in range(self.get_land_size("y"))]

    def set_board(self, board: list):
        self.game_board = copy.deepcopy(board)
        
    def get_board(self):
        return self.game_board

    def update_board(self):
        
        #
        # Write your code here
        #

        self.game_board

        self.update_board_in_gamestate()
        pass

    def show_board(self):
        # Currently here for debug purposes only.
        # Prints out the raw data not a beautified board.
        # The beautified board should be shown here
        print(self.get_board())

    # ------------
    # Game Actions
    # ------------

    def harvest(coordX: int, coordY: int):
        pass

    
    def plant(coordX: int, coordY: int, plantType: str):
        pass