"""
save.py

Game save/load
"""

import json
import pathlib

def save_game(fileName, gameState):
    """
    Saves game state into a file with name as specified in ./saves folder.

    Args:
        * fileName ('str'): The name of the save file
        * gameState ('dict'): Game state as a dictionary

    Returns:
        None
    """

    # Creates the "saves" directory if it doesn't exist
    dir_loc = pathlib.Path("./saves/")
    dir_loc.mkdir(parents=True, exist_ok=True)

    # Creates the save file if it doesn't exist
    file_loc = pathlib.Path("./saves/" + fileName + ".json")
    file_loc.touch(exist_ok=True)

    # Now open the file to write the data as json
    f = open(file_loc, "w+")
    json.dump(gameState, f)
    f.close()

    # Return success message
    return "Game has been saved to {}.".format(fileName)

def load_game(fileName):
    """
    Loads game state from a file with name as specified and returns it.

    Args:
        * fileName ('str'): The name of the save file

    Returns:
        * gameState ('dict'): Game state as a dictionary
    """

    try:
        file_loc = "./saves/" + fileName + ".json"
        f = open(file_loc, "r")
        gameState = json.load(f)
        f.close()
        return gameState
    except FileNotFoundError:
        print("File named '{}' cannot be found!".format(fileName))