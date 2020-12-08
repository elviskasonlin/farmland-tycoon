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
        menu_choice = AUXFN.get_user_choice(displayText=GUI.get_start_menu(), returnType="int")
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
        
        # Checks whether the game has ended
        while (Game.get_game_ended_flag() != True):
            # Get user command input
            user_input = AUXFN.get_user_choice(displayText="\n" + "-" * Game.get_game_output_width() + "\nCmd input: ", returnType="str").strip().split()
            user_command = user_input[0].lower()
            print(user_input)
            print(user_command)

            if (user_command == "help"):
                # Show help menu
                print(GUI.get_help_menu())
            elif (user_command == "plots"):
                # Debug: Currently only printing the raw board data
                print(Game.show_board())
            elif (user_command == "plant"):
                # Plant a crop
                try:
                    coord_x, coord_y = AUXFN.convert_coord_input(user_input[1])
                    coord_validity = Game.is_coord_valid(coordX=coord_x, coordY=coord_y)
                    plant_type = user_input[2]
                    plant_validity = Game.is_plant_valid(plantType=plant_type)
                except Exception:
                    print("Invalid input. Please input coordinates followed by a crop name like so: `1,1 apple`")
                    continue
                else:
                    print(plant_type)
                    print(plant_validity)
            elif (user_command == "harvest"):
                # Harvest a crop
                try:
                    coord_x, coord_y = AUXFN.convert_coord_input(user_input[1])
                    coord_validity = Game.is_coord_valid(coordX=coord_x, coordY=coord_y)
                except Exception:
                    print("Invalid coordinates. Please input coordinates like so: `1,1`")
                    continue
                else:
                    if (coord_validity == True):
                        Game.harvest(coordX=coord_x, coordY=coord_y)
                pass
            elif (user_command == "upgrade"):
                # Purchase upgrades
                upgrade_type = user_input[1]
                pass
            elif (user_command == "warehouse"):
                # Check warehouse
                pass
            elif (user_command == "sell"):
                # Sell off crops
                plant_type = user_input[1].lower()
                quantity = user_input[2]
                pass
            elif (user_command == "save"):
                # Save the game
                Game.save_game()
            elif (user_command == "exit"):
                # Exit the game
                u_choice = AUXFN.get_user_choice(displayText="Would you like to save? [Y] or [N]: ", returnType="str").strip().lower()
                if (u_choice == "y"):
                    Game.save_game()
                else:
                    pass
                break
            elif (user_command == "plants"):
                # Print out available plants
                pass
            elif (user_command == "upgrades"):
                # Print out available upgrades
                pass
        
            else:
                print("Invalid command. For a list of available commands, please type in `help`.")
                pass

            pass
    
    return

def main():
    """
    Main entry point for the program
    """

    menu_choice = -1
    while (menu_choice != 0):
        menu_choice = AUXFN.get_user_choice(displayText=GUI.get_main_menu(), returnType="int")

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