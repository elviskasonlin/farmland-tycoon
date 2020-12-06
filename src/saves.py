"""
saves.py

Provides functions to allow for reading/writing of game saves
"""

import json
import pathlib

def load_game(fileName):
    """
    Loads game state from a file with name as specified and returns it.

    Args:
        * fileName ('str'): The name of the save file

    Returns:
        * If successful, returns a tuple with the following:
            * 1 ('int'): An integer to flag that the operation was successful
            * gameState ('dict'): Game state as a dictionary
        * If there's an error, returns a tuple with the following:
            * 0 ('int'): An integer to flag that the operation was unsuccessful
            * Error message ('str'): A custom error message
    """

    try:
        # Sets up the default file location for simplicity
        file_loc = "." + "/saves/" + fileName + ".json"

        # Now open the json file to read the data
        f = open(file_loc, "r")
        gameState = json.load(f)
        f.close()

        # ... and return the game save data as a dictionary
        return (1, gameState)
    except FileNotFoundError as err:
        print(err)
        return (0, "File named '{}' cannot be found!".format(fileName))

def save_game(fileName, gameState):
    """
    Saves game state into a file with name as specified in ./saves folder.

    Args:
        * fileName ('str'): The name of the save file
        * gameState ('dict'): Game state as a dictionary

    Returns:
        * If successful, returns a tuple with the following:
            * 1 ('int'): An integer to flag that the operation was successful
            * Success message ('str'): A custom success message with save location
        * If there's an error, returns a tuple with the following:
            * 0 ('int'): An integer to flag that the operation was unsuccessful
            * Error message ('str'): A custom error message
    """

    try:
        # Setting up the default file location for simplicity
        # Creates the "saves" directory if it doesn't exist
        dir_loc = pathlib.Path("." + "/saves/")
        dir_loc.mkdir(parents=True, exist_ok=True)

        # Specifying the location of the save file (default to be in the parent folder)
        file_loc = pathlib.Path("." + "/saves/" + fileName + ".json")

        # Now open the file to write the data as json
        f = open(file_loc, "w+") # w is write mode. w+ creates a file if it doesn't exist
        json.dump(gameState, f)
        f.close()

        # Return success message
        return (1, "Game has been saved to {}.".format(file_loc))
    except Exception as err:
        print(err)
        return (0, "Game was not saved.")