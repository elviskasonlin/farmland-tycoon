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

    # Game state with default values
    game_state = {
        "days": 0,
        "climate": "",
        "land": {"size": None, "plots": None},
        "upgrades": {},
        "money": 0,
        "productivity": 1,
        "maintenance": 0,
        "warehouse": {}
        }

    # Contains the game_board. Once all operations are done,
    # Remember to copy this dictionary back into the game_state["land"]["plots"]
    game_board = {}

    # Dictionaries containing the types and values for each of the crops -
    # - and upgrades as defined in the configuraiton files
    available_crops = {}
    available_upgrades = {}

    # Flags
    game_ended_flag = False
    start_game_flag = False

    # Other variables
    game_ended_type = None
    game_output_width = 95
    current_turn_day_usage = 0

    # --------------
    # Initialisation
    # --------------

    def __init__(self):
        try:
            # Load the data for crops and upgrades as defined in the config files
            self.available_crops = AUXFN.load_configuration("default_crops")
            self.available_upgrades = AUXFN.load_configuration("default_upgrades")
        except Exception:
            raise Exception("Encountered error while loading configuration files.")

    # ----------
    # Core Stuff
    # ----------
    
    # +++++++++++++
    # Core: Getters
    # +++++++++++++

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
            * (`bool`): `True` if end condition is met. `False` if otherwise.
        """
        return self.game_ended_flag
    
    def get_game_ended_type(self):
        """
        Returns the type of condition the game has met

        Returns:
            * (`int` or `None`):  Default of `None`. `0` if player loses, `1` if player wins.
        """
        return self.game_ended_type

    def get_game_output_width(self):
        """
        Returns the max terminal output width as set previously

        Returns:
            (`int`): Max output width
        """
        return self.game_output_width
    
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
    
    def get_available_crops(self):
        """
        Returns the entire crop dictionary including attributes

        Returns:
            * (`dict`): All available crops
        """
        return self.available_crops

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

    def get_available_upgrades(self):
        """
        Returns the entire upgrades dictionary

        Returns:
            * (`dict`): All available upgrades including attributes
        """
        return self.available_upgrades
        
    def get_player_upgrades(self):
        """
        Gets player's current upgrades and returns it as a dictionary

        Returns:
            (`dict` or `None`): Returns a dict with filled entires if there's upgrades. Otherwise, returns `None`
        """

        output = dict()
        upgrades_as_dict = self.game_state["upgrades"]

        if (len(upgrades_as_dict) == 0):
            output = None
        else:
            output = copy.deepcopy(upgrades_as_dict)

        return output
    
    def get_warehouse_items(self):
        """
        Returns a list with the names and the corresponding amount of items currently stored in the warehouse.

        Returns:
            (`dict` or `None`): Returns a dict with filled entires if there's items stored. Otherwise, returns `None`
        """
        # Check warehouse items
        # Return what's inside the warehouse
        # If none, return `None`

        output = dict()
        warehouse_items_as_dict = self.game_state["warehouse"]

        if (len(warehouse_items_as_dict) == 0):
            output = None
        else:
            output = copy.deepcopy(warehouse_items_as_dict)

        return output

    def get_day_usage(self):
        pass

    # +++++++++++++
    # Core: Setters
    # +++++++++++++

    def set_game_output_width(self, width: int):
        """
        Sets the max terminal output width

        Args:
            width (int): Max terminal output width
        """
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

    def update_game_ended_condition(self):
        """
        Checks whether the end condition has been met.
        Then updates game_ended_flag and game_ended_type.
        """
        flag, type = None, None
        player_money = self.get_game_state()["money"]
        if (player_money <= 0):
            flag = True
            type = 0
        elif (player_money >= 1000000):
            flag = True
            type = 1
        else:
            flag = False
        self.game_ended_type = flag
        self.game_ended_flag = type
        return

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

    def is_crop_valid(self, cropName: str):
        """
        Checks whether the crop specified is a valid entry

        Args:
            cropName (str): The name of the crop to check.

        Returns:
            (`bool`): True if valid, False if it isn't
        """
        if (cropName not in self.get_available_crop_names()):
            return False
        else:
            return True

    def is_upgrade_valid(self, upgradeName: str):
        """
        Checks whether the upgrade name specified is a valid entry

        Args:
            upgradeName (str): The name of the upgrade

        Returns:
            (`bool`): True if valid, False if it isn't
        """
        if (upgradeName not in self.get_available_upgrade_names()):
            return False
        else:
            return True

    def is_plot_empty(self, xCoord: int, yCoord: int):
        """
        Checks if plot is empty at specified coordinates

        Args:
            xCoord (int): [description]
            yCoord (int): [description]
        """
        item_at_loc = self.game_board[xCoord][yCoord]
        pass

    def is_harvestable(self, xCoord: int, yCoord: int):
        self.check_crop_age(xCoord=xCoord, yCoord=yCoord)
        # check with the time it takes to harvest
        crop_at_loc = self.get_crop_at_loc(xCoord=xCoord, yCoord=yCoord)
        planted_timestamp = None
        time_since_planted = None
        if (time_since_planted == None):
            pass
        pass

    def check_crop_age(self, xCoord: int, yCoord: int):
        pass

    def get_crop_at_loc(self, xCoord: int, yCoord: int):
        pass

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

    def next_turn(self):
        # Remember to reset curent turn usage
        self.current_turn_day_usage = 0
        pass

    def harvest(self, coordX: int, coordY: int):
        """
        Harvests a crop at a given (x,y) coordinate

        Args:
            * coordX (`int`): x-coordinate on the board
            * coordY (`int`): y-coordinate on the board
        """
        # Checks whether the plot is not empty
        # Checks whether the crop can be harvested
        # Changes the plot to empty
        # Checks for player's land upgrade
        # DAY: Update time taken to crop by dividing with productivity value
        # Adds the crop to the warehouse multiplied by the yield 

        pass

    
    def plant(self, coordX: int, coordY: int, cropType: str):
        """
        Plants a crop at a given (x,y) coordinate

        Args:
            * coordX (`int`): x-coordinate on the board
            * coordY (`int`): y-coordinate on the board
            * cropType (`str`): The name of the crop to be planted
        """
        # Assumes that the cropType is valid. (Check done before calling this function)
        # Check whether the plot is empty
        # Check if the player can afford the crop
        # If all the conditions are met, plant the crop at the board
        # DAY: Update time taken to crop by dividing with productivity value
        # Synchronise board and board in game_state
        
        pass

    def purchase_upgrade(self, upgradeName: str):
        # Assumes that the upgradeName is valid. (Check done before calling this function)
        # Check if the player can afford the upgrade
        # If condition is met, purcahse the upgrade
        # Add count to the upgrade in game state
        # Modify productivity parameter
        # Modify maintainence parameter
        pass

    def sell_crop(self, cropName: str, quantity: int):
        # Assumes that the cropName is valid. (Check done before calling this function)
        # Check if the the crop quantity to be sold is enough

        warehouse_items = self.get_warehouse_items()
        # If not, don't do anything. Show error message
        # If yes, reduce crop quantity. Increase player money by the qty * sell price
        pass