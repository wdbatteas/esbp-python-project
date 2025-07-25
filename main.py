import sys
import terminalLib as terminal
import customerLib
import inventoryLib


class GameState:
    def __init__(self):
        self.game_name = "Manage your store"
        self.store_balance = 1000.0
        self.store_rating = 4.0
        self.store_day = 0
        self.store_tick_count = 0
        self.store_ticks_per_day = 10
        self.store_name = ""
        self.store_difficulty = ""
        self.game_is_running = True
        self.fast_forward = False
        self.event_messages = []
        self.store_inv = None
        self.customer_distribution = []
        self.current_tick_customer = None



def check_platform():
    # https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on
    import platform
    if platform.system() != "Windows":
        print("Game is not designed to run on linux. Press enter to continue.")
        terminal.waitUntilEnter()

def starting_menu(game_state):
    startingMenu = ["Play Sandbox", "Play Story Mode", "Exit"]
    startingMenuWarningMessage = None
    while True:
        response = terminal.askMenu(game_state.game_name, startingMenu, warningMessage=startingMenuWarningMessage)
        if response == startingMenu[0]:
            break
        elif response == startingMenu[1]:
            startingMenuWarningMessage = f"{terminal.color.BRIGHT_RED}Story Mode is Currently Disabled{terminal.color.RESET}"
        elif response == startingMenu[2]:
            sys.exit()

def ask_difficulty(game_state):
    valid_options = ["Easy", "Medium", "Hard", "Insane"]
    return terminal.askMenu(game_state.game_name, valid_options, promptText="Select a difficulty level for the game.")

def get_store_name(game_state):
    storeNamePrompt = [
        "You're beginning a business."
        "What do you want the name to be?"
    ]
    game_state.store_name = terminal.askForInput(game_state.game_name, storeNamePrompt)

def starter_inventory():
    inv = inventoryLib.Inventory()
    return inv

def print_opening_summary(game_state):
    to_draw = [
        f"{terminal.color.BRIGHT_CYAN}Welcome to {game_state.store_name}!{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_GREEN}Store Balance: ${game_state.store_balance:.2f}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_YELLOW}Store Rating: {game_state.store_rating} stars{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_MAGENTA}Day: {game_state.store_day}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_WHITE}Press Enter to continue...{terminal.color.RESET}"
    ]
    

    terminal.drawWindowBuffered(game_state.game_name, to_draw)

    # go to start of line to avoid typing anything and going to new line
    terminal.format.gotoXY(0, terminal.getTerminalHeight() - 1)

    terminal.waitUntilEnter()


def print_closing_summary(game_state):
    to_draw = [
        f"{terminal.color.BRIGHT_RED} END OF DAY {terminal.color.RESET}",
        f"{terminal.color.BRIGHT_CYAN}Leaving {game_state.store_name}!{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_GREEN}Store Balance: ${game_state.store_balance:.2f}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_YELLOW}Store Rating: {game_state.store_rating} stars{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_MAGENTA}Day: {game_state.store_day}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_WHITE}Press Enter to continue...{terminal.color.RESET}"
    ]
    

    terminal.drawWindowBuffered(game_state.game_name, to_draw)

    # go to start of line to avoid typing anything and going to new line
    terminal.format.gotoXY(0, terminal.getTerminalHeight() - 1)

    terminal.waitUntilEnter()

def do_tick_menu(game_state):
    in_menu = True
    while in_menu:
        valid_options = [
            "Buy Inventory", 
            "Set Prices", 
            "Upgrade Store", 
            "View Details About Store", 
            "Continue to Next Game Event", 
            "End Day", 
            "Exit Game"
            ]
        
        prompt_text = [f"Current Tick: {game_state.store_tick_count}","Please choose an option:"]
        
        if game_state.event_messages:
            prompt_text = game_state.event_messages + prompt_text
            game_state.event_messages = []
        
        response = terminal.askMenu(game_state.game_name, valid_options, promptText=prompt_text)

        if response == "Buy Inventory":
            handle_buy_inventory(game_state)

        elif response == "Set Prices":
            handle_set_prices(game_state)

        elif response == "Upgrade Store":
            handle_upgrade_store(game_state)

        elif response == "View Details About Store":
            handle_print_details(game_state)

        elif response == "Continue to Next Game Event":
            in_menu = False

        elif response == "End Day (fast fowards)":
            game_state.fast_forward = True
            in_menu = False

        elif response == "Talk To A Customer":
            handle_talk_customer(game_state)

        elif response == "Exit Game":
            in_menu = handle_exit(game_state)


def handle_buy_inventory(game_state):
    valid_options = ["Check Inventory", "Buy an Item", "Back"]
    response = terminal.askMenu(game_state.game_name, valid_options)
    if response == "Buy an Item":
        pass
    elif response == "Check Inventory":
        pass # print all items in window
    elif response == "Back":
        pass
    pass

def handle_set_prices(game_state):
    pass

def handle_upgrade_store(game_state):
    pass

def handle_print_details(game_state):
    pass

def handle_talk_customer(game_state):
    pass

def handle_exit(game_state):
    valid_choices = ["Yes", "No"]
    message = ["Are you sure you want to exit?", "The game does not save data"]
    response = terminal.askMenu(game_state.game_name, valid_choices, message)
    if response == "Yes":
        game_state.game_is_running = False
        return False
    return True

def do_customer_shopping(game_state):
    # handle customer shopping
    tick_index = game_state.store_tick_count - 1
    
    game_state.current_tick_customer = game_state.customer_distribution[tick_index]
    if type(game_state.current_tick_customer) == customerLib.Customer:
        # customerLib.customer_shops(current_tick_customer, store_inv)
        game_state.event_messages.append(f"{game_state.current_tick_customer} is shopping")

    elif type(game_state.current_tick_customer) == list:
        for cust in game_state.current_tick_customer:
            # customerLib.customer_shops(cust, store_inv)
            game_state.event_messages.append(f"{game_state.current_tick_customer} is shopping")
    elif type(game_state.current_tick_customer) == None:
            pass

# game phases
def start_day(game_state):
    # generate customers for the day
    customers = customerLib.spawn_customers(game_state.store_day, game_state.store_rating, game_state.store_difficulty)

    # generate customer shopping distribution
    game_state.customer_distribution = customerLib.get_customer_shop_distribution(customers, game_state.store_ticks_per_day)
    

    # print opening summary
    print_opening_summary(game_state)

    # let user do actions
    do_tick_menu(game_state)

def handle_shopping_phase(game_state):
    if game_state.fast_forward == True:
        while game_state.store_tick_count < game_state.store_ticks_per_day:
            do_customer_shopping(game_state)
            game_state.store_tick_count += 1
    else:
        do_customer_shopping(game_state)
        

    do_tick_menu(game_state)
    game_state.store_tick_count += 1


def end_day(game_state):
    print_closing_summary(game_state)
    game_state.store_tick_count = 0
    game_state.store_day += 1
    game_state.event_messages = []

def main():
    check_platform()
    terminal.format.hideCursor()
    game_state = GameState()

    starting_menu(game_state)
    ask_difficulty(game_state)
    get_store_name(game_state)
    game_state.store_inv = starter_inventory()

    # game loop
    while game_state.game_is_running:
        if game_state.store_tick_count == 0:
            start_day(game_state)
            game_state.store_tick_count += 1
        elif game_state.store_tick_count >= 1 and game_state.store_tick_count <= game_state.store_ticks_per_day:
            handle_shopping_phase(game_state)
        elif game_state.store_tick_count == (game_state.store_ticks_per_day + 1):
            end_day(game_state)
        else:
            raise Exception(f"Unknown error: {game_state.store_tick_count} is not in range 0-{game_state.store_ticks_per_day}")
    
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()