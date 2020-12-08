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
        else:
            pass
    
    # -------------------
    # Start the game loop
    # -------------------
    if (Game.get_start_flag() == True):
        
        # Checks whether the game has ended
        while (Game.get_game_ended_flag() != True):
            # Get user command input
            print("\n" + "-" * Game.get_game_output_width() + "\n")
            print("Current turn usage (Max 7): ", Game.get_turn_day_usage())
            user_input = AUXFN.get_user_choice(displayText="\nCmd input: ", returnType="str").strip().split()
            user_command = user_input[0].lower()

            # ---------------------
            # Handle command inputs
            # ---------------------

            if (user_command == "help"):
                # ============
                # ACTION: Help
                # ============
                # Show help menu
                print(GUI.get_help_menu())

            elif (user_command == "plots" or user_command == "p"):
                # =============
                # ACTION: Plots
                # =============
                # Shows the game board 
                print(Game.get_beautified_board())

            elif (user_command == "plant"):
                # =============
                # ACTION: Plant
                # =============
                # Plant a crop
                try:
                    coord_x, coord_y = AUXFN.convert_coord_input(user_input[1])
                    coord_validity = Game.is_coord_valid(coordX=coord_x, coordY=coord_y)
                    crop_name = user_input[2].lower()
                    crop_validity = Game.is_crop_valid(cropName=crop_name)
                except Exception:
                    print("Invalid input. Please input coordinates followed by a crop name like so: `1,1 apple`")
                    continue
                else:
                    if (coord_validity == True and crop_validity == True):
                        Game.plant(coordX=coord_x, coordY=coord_y, cropType=crop_name)
                pass

            elif (user_command == "harvest"):
                # ===============
                # ACTION: Harvest
                # ===============
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
                # ===============
                # ACTION: Upgrade
                # ===============
                # Purchase upgrades

                try:
                    upgrade_name = user_input[1].lower()
                    upgrade_validity = Game.is_upgrade_valid(upgradeName=upgrade_name)
                except Exception:
                    print("Invalid input. Please input your command like so: `upgrade land`")
                else:
                    if (upgrade_validity == True):
                        Game.purchase_upgrade(upgrade_name)
                pass

            elif (user_command == "purchased"):
                # ===============
                # ACTION: Purchased
                # ===============
                # Lists purchased upgrades

                upgrades = Game.get_player_upgrades()
                print("Upgrades variable: ")
                print(upgrades)
                if (upgrades != None):
                    print(GUI.print_beautified_dictionary(upgrades))
                else:
                    print("You have no upgrades purchased.")
                pass

            elif (user_command == "warehouse"):
                # Done
                # =================
                # ACTION: Warehouse
                # =================
                # Check warehouse and print items in the warehouse

                warehouse_items = Game.get_warehouse_items()
                if (warehouse_items != None):
                    print(GUI.print_beautified_dictionary(warehouse_items))
                else:
                    print("The warehouse is empty.")
                pass

            elif (user_command == "sell"):
                # ============
                # ACTION: Sell
                # ============
                # Sell off crops

                try:
                    crop_name = user_input[1].lower()
                    quantity = user_input[2]
                    plant_validity = Game.is_crop_valid(cropName=crop_name)
                    qty_validity = quantity.isdigit()
                except Exception:
                    print("Invalid input. Please input your command like so: `sell apple 5`")
                else:
                    if (plant_validity == True and qty_validity == True):
                        Game.sell_crop(cropName=crop_name, quantity=quantity)
                pass

            elif (user_command == "next" or user_command == "n"):
                Game.next_turn()

            elif (user_command == "save"):
                # ============
                # ACTION: Save
                # ============
                # Save the game
                Game.save_game()

            elif (user_command == "exit"):
                # ============
                # ACTION: Exit
                # ============
                # Exit the game
                u_choice = AUXFN.get_user_choice(displayText="Would you like to save? [Y] or [N]: ", returnType="str").strip().lower()
                if (u_choice == "y"):
                    Game.save_game()
                else:
                    pass
                break

            elif (user_command == "crops"):
                # ==============
                # ACTION: Crops
                # ==============
                # Print out available crops
                print("Available crops:\n", GUI.print_available(dictionary=Game.get_available_crops(), type="crop"))
                pass

            elif (user_command == "upgrades"):
                # ================
                # ACTION: Upgrades
                # ================
                # Print out available upgrades
                print("Available upgrades:\n", GUI.print_available(dictionary=Game.get_available_upgrades(), type="upgrade"))
                pass

            elif (user_command == "debug"):
                # REMEMBER TO REMOVE THIS FROM PRODUCTION
                # For general debug stuff.
                pass

            else:
                print("Invalid command. For a list of available commands, please type in `help`.")
                pass
            # end of if statement

            # Check whether this turn should end
            if (Game.should_next_turn() == True):
                Game.next_turn()
                Game.update_game_ended_condition()

            pass # end of while loop
        # end of game loop
    return # end of start()

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