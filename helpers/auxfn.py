"""
auxfn.py

Auxilliary functions
"""

def get_user_choice(display_text, return_type):
    """
    Gets the user's choice using input()

    Args:
        * display_text (`str`): The text to be displayed in `input()`
        * return_type (`str`): The target conversion.

    Returns:
        * user_input (`str`, `bool`, `int`, `float`): The user's input converted to the target type as specified in `return_type`
    """

    buffer = input(display_text)
    output = None

    try:
        if (return_type == "float"):
            output = float(buffer) 
        elif (return_type == "int"):
            output = int(buffer)
        elif (return_type == "bool"):
            output = bool(int(buffer))
        else:
            output = buffer
        pass
    except Exception as err:
        print(err)

    return output
