import sys
import terminalLib as terminal
import customerLib
import inventoryTranslationLib as invLib
from itemLib import *
import storageLib



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
    difficulty_menu = ["Easy", "Medium", "Hard", "Insane"]
    difficult_menu_warning = None
    while True:
        response = terminal.askMenu(game_state.game_name, difficulty_menu, warningMessage=difficult_menu_warning)
        if response == difficulty_menu[0]:
            break
        elif response == difficulty_menu[1]:
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Medium is Currently Disabled{terminal.color.RESET}"
        elif response == difficulty_menu[2]:
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Hard is Currently Disabled{terminal.color.RESET}"
        elif response == difficulty_menu[3]:
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Insane is Currently Disabled{terminal.color.RESET}"

    return "Easy"
    # valid_options = ["Easy", "Medium", "Hard", "Insane"]
    # return terminal.askMenu(game_state.game_name, valid_options, promptText="Select a difficulty level for the game.")

def get_store_name(game_state):
    storeNamePrompt = [
        "You're beginning a business."
        "What do you want the name to be?"
    ]
    response = terminal.askForInput(game_state.game_name, storeNamePrompt)
    if response:
        game_state.store_name = response
    else:
        game_state.store_name = "This store was not named"

def update_store_rating(game_state, customer_satisfaction_scores):
    """Update store rating based on customer satisfaction"""
    if customer_satisfaction_scores:
        avg_satisfaction = sum(customer_satisfaction_scores) / len(customer_satisfaction_scores)
        # Gradually adjust rating towards satisfaction level
        rating_change = (avg_satisfaction - 0.5) * 0.1  # Scale to reasonable change
        game_state.store_rating = max(0.0, min(5.0, game_state.store_rating + rating_change))
        
def starter_inventory(game_state):
    return invLib.create_starter_inventory(game_state.store_difficulty)

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
            "End Day (fast foward)", 
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

        elif response == "End Day (fast foward)":
            game_state.fast_forward = True
            in_menu = False

        elif response == "Talk To A Customer":
            handle_talk_customer(game_state)

        elif response == "Exit Game":
            in_menu = handle_exit(game_state)


def handle_buy_inventory(game_state):
    valid_options = ["Check Inventory", "Buy an Item", "Back"]
    response = terminal.askMenu(game_state.game_name, valid_options)
    
    if response == "Check Inventory":
        summary = invLib.get_inventory_summary(game_state.store_inv)
        inventory_display = [
            f"Stock: {summary['stock']}/{summary['capacity']}",
            f"Free Space: {summary['free_space']}",
            f"Items in stock: {summary['items_count']}",
            ""
        ]
        for name, count, price in summary['items']:
            inventory_display.append(f"{name} x{count} (${price:.2f} each)")
        
        terminal.drawWindowBuffered(game_state.game_name, inventory_display)
        terminal.waitUntilEnter()
        
    elif response == "Buy an Item":
        buyable_items = invLib.get_buyable_items()
        buyable_items.append("Back")
        
        item_choice = terminal.askMenu(game_state.game_name, buyable_items, "What item would you like to buy?")
        if item_choice != "Back":
            quantity_prompt = [f"How many {item_choice} would you like to buy?", f"Cost per item: ${catalog[item_choice]['purchaseCost']:.2f}"]
            try:
                quantity_str = terminal.askForInput(game_state.game_name, quantity_prompt)
                quantity = int(quantity_str)
                
                success, cost, message = invLib.buy_item_for_inventory(game_state.store_inv, item_choice, quantity, game_state)
                game_state.event_messages.append(message)
                if success:
                    game_state.event_messages.append(f"Spent ${cost:.2f}")
                    
            except ValueError:
                game_state.event_messages.append("Invalid quantity entered")

def handle_set_prices(game_state):
    summary = invLib.get_inventory_summary(game_state.store_inv)
    if not summary['items']:
        game_state.event_messages.append("No items in inventory to price")
        return
    
    item_names = [item[0] for item in summary['items']]
    item_names.append("Back")
    
    item_choice = terminal.askMenu(game_state.game_name, item_names, "Which item would you like to price?")
    if item_choice != "Back":
        current_item = None
        for item in game_state.store_inv.listItems():
            if item.getName() == item_choice:
                current_item = item
                break
        
        if current_item:
            price_prompt = [
                f"Current price for {item_choice}: ${current_item.getSellValue():.2f}",
                f"Purchase cost: ${current_item.getPurchaseCost():.2f}",
                "Enter new selling price:"
            ]
            try:
                new_price_str = terminal.askForInput(game_state.game_name, price_prompt)
                new_price = float(new_price_str)
                if new_price > 0:
                    invLib.set_item_price(game_state.store_inv, item_choice, new_price)
                    game_state.event_messages.append(f"Set {item_choice} price to ${new_price:.2f}")
                else:
                    game_state.event_messages.append("Price must be positive")
            except ValueError:
                game_state.event_messages.append("Invalid price entered")

def handle_upgrade_store(game_state):
    upgrade_options = ["Buy Storage Unit", "Upgrade Existing Storage", "Back"]
    response = terminal.askMenu(game_state.game_name, upgrade_options)
    
    if response == "Buy Storage Unit":
        available_units = ["shelf", "freezer", "Back"]
        unit_choice = terminal.askMenu(game_state.game_name, available_units, "What storage would you like to buy?")
        
        if unit_choice != "Back":
            cost = storageLib.units[unit_choice]['purchaseCost']
            if game_state.store_balance >= cost:
                new_unit = storageLib.StorageUnit(unit_choice)
                success = game_state.store_inv.addStorageUnit(new_unit)
                if success:
                    game_state.store_balance -= cost
                    game_state.event_messages.append(f"Bought {unit_choice} for ${cost}")
                else:
                    game_state.event_messages.append("Cannot add this storage unit")
            else:
                game_state.event_messages.append("Not enough money")

def handle_print_details(game_state):
    summary = invLib.get_inventory_summary(game_state.store_inv)
    details = [
        f"Store: {game_state.store_name}",
        f"Balance: ${game_state.store_balance:.2f}",
        f"Rating: {game_state.store_rating} stars",
        f"Day: {game_state.store_day}",
        f"Inventory: {summary['stock']}/{summary['capacity']}",
        "",
        "Items in stock:"
    ]
    
    for name, count, price in summary['items']:
        profit_margin = ((price - catalog[name]['purchaseCost']) / catalog[name]['purchaseCost']) * 100
        details.append(f"  {name}: {count}x @ ${price:.2f} ({profit_margin:.1f}% markup)")
    
    if game_state.store_inv.getStorageUnits():
        details.append("")
        details.append("Storage Units:")
        for unit in game_state.store_inv.getStorageUnits():
            details.append(f"  {unit}")
    
    terminal.drawWindowBuffered(game_state.game_name, details)
    terminal.waitUntilEnter()

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

# def do_customer_shopping(game_state):
#     # handle customer shopping
#     tick_index = game_state.store_tick_count - 1
    
#     game_state.current_tick_customer = game_state.customer_distribution[tick_index]
#     if type(game_state.current_tick_customer) == customerLib.Customer:
#         # customerLib.customer_shops(current_tick_customer, store_inv)
#         game_state.event_messages.append(f"{game_state.current_tick_customer} is shopping")

#     elif type(game_state.current_tick_customer) == list:
#         for cust in game_state.current_tick_customer:
#             # customerLib.customer_shops(cust, store_inv)
#             game_state.event_messages.append(f"{game_state.current_tick_customer} is shopping")
#     elif type(game_state.current_tick_customer) == None:
#             pass

# def do_customer_shopping(game_state):
#     tick_index = game_state.store_tick_count - 1
    
#     game_state.current_tick_customer = game_state.customer_distribution[tick_index]
#     if type(game_state.current_tick_customer) == customerLib.Customer:
#         customer = game_state.current_tick_customer
#         compatible_items = invLib.get_customer_compatible_items(game_state.store_inv, customer.preferences)
        
#         total_spent = 0
#         items_bought = []
        
#         for item_data in compatible_items:
#             if customer.budget >= item_data['price'] and item_data['stock'] > 0:
#                 success, revenue, message = invLib.sell_item_from_inventory(
#                     game_state.store_inv, 
#                     item_data['name'], 
#                     1, 
#                     customer.budget
#                 )
#                 if success:
#                     customer.budget -= revenue
#                     total_spent += revenue
#                     game_state.store_balance += revenue
#                     items_bought.append(item_data['name'])
        
#         if items_bought:
#             game_state.event_messages.append(f"Customer bought: {', '.join(items_bought)} (${total_spent:.2f})")
#         else:
#             game_state.event_messages.append("Customer left without buying anything")

#     elif type(game_state.current_tick_customer) == list:
#         for customer in game_state.current_tick_customer:
#             # Handle multiple customers (simplified - you may want to expand this)
#             game_state.event_messages.append(f"Multiple customers shopping")



def do_customer_shopping(game_state):
    tick_index = game_state.store_tick_count - 1
    
    if tick_index >= len(game_state.customer_distribution):
        return
        
    game_state.current_tick_customer = game_state.customer_distribution[tick_index]
    
    if isinstance(game_state.current_tick_customer, customerLib.Customer):
        customer = game_state.current_tick_customer
        compatible_items = invLib.get_customer_compatible_items(game_state.store_inv, customer.preferences)
        
        total_spent = 0
        items_bought = []
        
        # https://stackoverflow.com/questions/16310015/what-does-this-mean-key-lambda-x-x1
        compatible_items.sort(key=lambda x: x['price'])
        
        for item_data in compatible_items:
            if customer.budget >= item_data['price'] and item_data['stock'] > 0:
                success, revenue, message = invLib.sell_item_from_inventory(
                    game_state.store_inv, 
                    item_data['name'], 
                    1, 
                    customer.budget
                )
                if success:
                    customer.budget -= revenue
                    total_spent += revenue
                    game_state.store_balance += revenue
                    items_bought.append(item_data['name'])
        
        if items_bought:
            game_state.event_messages.append(f"Customer bought: {', '.join(items_bought)} (${total_spent:.2f})")
        else:
            game_state.event_messages.append("Customer left without buying anything")
            
    elif isinstance(game_state.current_tick_customer, list):
        for customer in game_state.current_tick_customer:
            # Process each customer in the group
            # (recursively call with single customer)
            temp_state = type('temp', (), {})()
            temp_state.store_inv = game_state.store_inv
            temp_state.store_balance = game_state.store_balance
            temp_state.event_messages = []
            temp_state.current_tick_customer = customer
            temp_state.store_tick_count = game_state.store_tick_count
            temp_state.customer_distribution = [customer]
            
            do_customer_shopping(temp_state)
            game_state.store_balance = temp_state.store_balance
            game_state.event_messages.extend(temp_state.event_messages)

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
        while game_state.store_tick_count <= game_state.store_ticks_per_day:
            do_customer_shopping(game_state)
            game_state.store_tick_count += 1
        game_state.fast_forward = False
    else:
        do_customer_shopping(game_state)
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
    game_state.store_inv = starter_inventory(game_state)

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