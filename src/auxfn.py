"""
auxfn.py

Auxilliary functions
"""

def get_user_choice(displayText: str, returnType: str):
    """
    Gets the user's choice using input()

    Args:
        * display_text (`str`): The text to be displayed in `input()`
        * return_type (`str`): The target conversion.

    Returns:
        * user_input (`str`, `bool`, `int`, `float`): The user's input converted to the target type as specified in `return_type`
    """

    buffer = input(displayText)
    output = None

    try:
        if (returnType == "float"):
            output = float(buffer) 
        elif (returnType == "int"):
            output = int(buffer)
        elif (returnType == "bool"):
            output = bool(int(buffer))
        else:
            output = buffer
    except Exception as err:
        print(err)
        pass

    return output


def settings():
    """
    Sets game settings

    Args:
        * None
    
    Returns:
        * None
    """
    print("settings() called. Settings to be set.")
    pass