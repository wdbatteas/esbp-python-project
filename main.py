import terminalLib as terminal
import os, sys
import customerLib as customerLib
import ssLib as game
import itemLib as item
import inventoryLib as inventory
import storageLib as storage


# import inventoryLib as inventory
# import fileLib as file
# import dummyStore as store

# try:
#     import animationLib as animation
#     animation.playLoadingIntro()
# except:
#     pass

# hide cursor
terminal.format.hideCursor()


game_name = "Shopping Simulator"

game.starting_menu(game_name)

store_difficulty = game.ask_difficulty(game_name)


# ===== Set up all variables
store_balance = 100.0
store_rating = 4.0
store_day = 0
store_tick_count = 1 
store_ticks_per_day = 20 # disable ticking system for now

store_name = game.get_store_name(game_name)

store_variables = [game_name, store_balance, store_rating, store_tick_count, store_ticks_per_day, store_name]
store_variables_start = []
store_variables_day = []

# create inventory
store_inv = game.starter_inventory()

# game loop
game_is_running = True
in_menu = False


while game_is_running:
    store_variables_start.append(store_variables.copy()) # Store starting variables to have reference to start

    game.print_opening_summary()

    # generate customers for the day
    customers = customerLib.spawn_customers(store_day, store_rating, store_difficulty)

    # generate customer shopping distribution
    customer_distribution = customerLib.get_customer_shop_distribution(customers, store_ticks_per_day)

    # enter a menu
    in_menu = True
    while in_menu:
        valid_options = ["Buy Inventory", "Set Prices", "Upgrade Store", "View Details About Store", "Continue to Next Game Event", "End Day", "Exit"]
        response = terminal.askMenu(game_name, valid_options)

        if response == "Buy Inventory":
            valid_options = ["Check Inventory", "Buy an Item", "Back"]
            response = terminal.askMenu(game_name, valid_options)
            if response == "Buy an Item":
                pass
            elif response == "Check Inventory":
                pass # print all items in window
            elif response == "Back":
                pass

        elif response == "Set Prices":
            pass # get all items, and print, and add option to go back

        elif response == "Upgrade Store":
            valid_options = ["Check Store", "Check Inventory", "Back"]
            response = terminal.askMenu(game_name, valid_options)

        elif response == "View Details About Store":
            # print inventory count, and item count, and store details
            pass

        elif response == "Continue to Next Game Event":
            store_tick_count += 1

        elif response == "End Day (skip ticks)":
            pass # ignore for now

        elif response == "Exit Game":
            game.exit()
    
    # exited menu
    
    # do customer shopping
    if store_tick_count == 0: 
        pass # customer cannot shop here
    elif store_tick_count > 0 and store_tick_count < 20:
        # get customer
        current_tick_customer = customer_distribution[store_tick_count]
    elif store_tick_count == 20:
        pass
    else: # unknown thing happened
        raise Exception()

    



    # game.printDailySummary(store_variables, store_variables_start) 