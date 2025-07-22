import terminalLib as terminal
import inventoryLib as inventory
import sys




def starting_menu(game_name):
    startingMenu = ["Play Sandbox", "Play Story Mode", "Exit"]
    startingMenuWarningMessage = None
    while True:
        
        response = terminal.askMenu(game_name, startingMenu, warningMessage=startingMenuWarningMessage)
        if response == startingMenu[0]:
            break
        elif response == startingMenu[1]:
            startingMenuWarningMessage = f"{terminal.color.BRIGHT_RED}Story Mode is Currently Disabled{terminal.color.RESET}"
        elif response == startingMenu[2]:
            sys.exit()

def ask_difficulty(game_name):
    valid_options = ["Easy", "Medium", "Hard", "Insane"]
    return terminal.askMenu(game_name, valid_options, promptText="Select a difficulty level for the game.")


def get_store_name(game_name):
    storeNamePrompt = [
        "You're beginning a business."
        "What do you want the name to be?"
    ]
    return terminal.askForInput(game_name, storeNamePrompt)


def exit():
    
    sys.exit()

def print_opening_summary(variable: list, store_day: int):
    # store_variables = [game_name, store_balance, store_rating, tick_count, store_name]
    # unpack
    current_day_variable = variable[store_day]

    # split
    game_name = current_day_variable[0]
    store_balance = current_day_variable[1]
    store_rating = current_day_variable[2]
    tick_count = current_day_variable[3]
    store_name = current_day_variable[4]

    # create window
    to_draw = [
        f'{terminal.color.BRIGHT_CYAN}Welcome to {game_name}!{terminal.color.RESET}',
        f'{terminal.color.BRIGHT_GREEN}Store Balance: ${store_balance:.2f}{terminal.color.RESET}',
        f'{terminal.color.BRIGHT_YELLOW}Store Rating: {store_rating} stars{terminal.color.RESET}',
        f'{terminal.color.BRIGHT_MAGENTA}Day: {tick_count}{terminal.color.RESET}',
        f'{terminal.color.BRIGHT_BLUE}Store Name: {store_name}{terminal.color.RESET}',
        f'{terminal.color.BRIGHT_WHITE}Press Enter to continue...{terminal.color.RESET}'
    ]

    terminal.drawWindowBuffered(game_name, to_draw)
    terminal.waitUntilEnter()


def wait(seconds: int):
    terminal.wait(seconds)


def starter_inventory():
    # create inventory
    inv = inventory.Inventory()

    inv.addAvailableStorage("Shelf", 100)
    inv.addAvailableStorage("Freezer", 100) # allow adding freezer with storage capacity of 100
    inv.addAvailableItem("Apple", "Shelf", 2) # apple allowed on shelf only and costs $2
    
    # add shelf to inventory
    inv.addStorage("Shelf")

    # add fridge to inventory
    inv.addStorage("Fridge")

    # add 5 items
    inv.addItems("Apple", 5)

    # test print count of all itmes
    print(inv.listItems())

    # test print storages
    print(inv.listStorages())

