import animationLib as anim

anim.playIntro()


import sys
import terminalLib as terminal
from terminalLib import log
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
    log("Checking platform compatibility...")
    # https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on
    import platform
    if platform.system() != "Windows":
        print("Game is not designed to run on linux. Press enter to continue.")
        terminal.waitUntilEnter()

def starting_menu(game_state):
    log("Displaying starting menu...")
    startingMenu = ["Play Sandbox", "Play Story Mode", "Exit"]
    startingMenuWarningMessage = None
    while True:
        response = terminal.askMenu(game_state.game_name, startingMenu, warningMessage=startingMenuWarningMessage)
        if response == startingMenu[0]:
            log("User selected Play Sandbox")
            break
        elif response == startingMenu[1]:
            log("User selected Play Story Mode")
            startingMenuWarningMessage = f"{terminal.color.BRIGHT_RED}Story Mode is Currently Disabled{terminal.color.RESET}"
        elif response == startingMenu[2]:
            log("User selected Exit")
            sys.exit()

def ask_difficulty(game_state):
    log("Asking for game difficulty...")
    difficulty_menu = ["Easy", "Medium", "Hard", "Insane"]
    difficult_menu_warning = None
    while True:
        response = terminal.askMenu(game_state.game_name, difficulty_menu, warningMessage=difficult_menu_warning)
        if response == difficulty_menu[0]:
            log("User selected Easy difficulty")
            break
        elif response == difficulty_menu[1]:
            log("User selected Medium difficulty")
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Medium is Currently Disabled{terminal.color.RESET}"
        elif response == difficulty_menu[2]:
            log("User selected Hard difficulty")
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Hard is Currently Disabled{terminal.color.RESET}"
        elif response == difficulty_menu[3]:
            log("User selected Insane difficulty")
            difficult_menu_warning = f"{terminal.color.BRIGHT_RED}Insane is Currently Disabled{terminal.color.RESET}"

    return "Easy"
    # valid_options = ["Easy", "Medium", "Hard", "Insane"]
    # return terminal.askMenu(game_state.game_name, valid_options, promptText="Select a difficulty level for the game.")

def get_store_name(game_state):
    log("Getting store name from user...")
    storeNamePrompt = [
        "You're beginning a business."
        "What do you want the name to be?"
    ]
    response = terminal.askForInput(game_state.game_name, storeNamePrompt)
    if response:
        log(f"User provided store name: {response}")
        game_state.store_name = response
    else:
        log("User did not provide a store name, using default.")
        game_state.store_name = "This store was not named"

def update_store_rating(game_state, customer_satisfaction_scores):
    log(f"Updating store rating based on customer satisfaction scores: {customer_satisfaction_scores}")
    """Update store rating based on customer satisfaction"""
    if customer_satisfaction_scores:
        avg_satisfaction = sum(customer_satisfaction_scores) / len(customer_satisfaction_scores)
        log(f"Average customer satisfaction: {avg_satisfaction}")
        # Gradually adjust rating towards satisfaction level
        rating_change = (avg_satisfaction - 0.5) * 0.1  # Scale to reasonable change
        log(f"Rating change calculated: {rating_change}")
        game_state.store_rating = max(0.0, min(5.0, game_state.store_rating + rating_change))
        log(f"New store rating: {game_state.store_rating}")
        
def starter_inventory(game_state):
    log("Creating starter inventory...")
    return invLib.create_starter_inventory(game_state.store_difficulty)

def print_opening_summary(game_state):
    log("Printing opening summary...")
    to_draw = [
        f"{terminal.color.BRIGHT_CYAN}Welcome to {game_state.store_name}!{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_GREEN}Store Balance: ${game_state.store_balance:.2f}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_YELLOW}Store Rating: {game_state.store_rating} stars{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_MAGENTA}Day: {game_state.store_day}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_WHITE}Press Enter to continue...{terminal.color.RESET}"
    ]
    log(f"Drawing opening summary: {to_draw}")
    

    terminal.drawWindowBuffered(game_state.game_name, to_draw)

    # go to start of line to avoid typing anything and going to new line
    terminal.format.gotoXY(0, terminal.getTerminalHeight() - 1)
    log("Waiting for user to press Enter...")
    terminal.waitUntilEnter()
    log("User pressed Enter.")


def print_closing_summary(game_state):
    log("Printing closing summary...")
    to_draw = [
        f"{terminal.color.BRIGHT_RED} END OF DAY {terminal.color.RESET}",
        f"{terminal.color.BRIGHT_CYAN}Leaving {game_state.store_name}!{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_GREEN}Store Balance: ${game_state.store_balance:.2f}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_YELLOW}Store Rating: {game_state.store_rating} stars{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_MAGENTA}Day: {game_state.store_day}{terminal.color.RESET}",
        f"{terminal.color.BRIGHT_WHITE}Press Enter to continue...{terminal.color.RESET}"
    ]
    log(f"Drawing closing summary: {to_draw}")
    

    terminal.drawWindowBuffered(game_state.game_name, to_draw)

    # go to start of line to avoid typing anything and going to new line
    terminal.format.gotoXY(0, terminal.getTerminalHeight() - 1)
    log("Waiting for user to press Enter...")
    terminal.waitUntilEnter()
    log("User pressed Enter, closing summary displayed.")

def do_tick_menu(game_state):
    log("Entering tick menu...")
    in_menu = True
    while in_menu:
        valid_options = [
            "Buy Inventory", 
            "Set Prices", 
            "Upgrade Store", 
            "View Details About Store", 
            "Continue to Next Hour", 
            "End Day (fast foward)", 
            "Talk To A Customer",
            "Exit Game"
            ]
        
        prompt_text = [f"Current Tick: {game_state.store_tick_count}","Please choose an option:"]
        log(f"Current tick: {game_state.store_tick_count}, available options: {valid_options}")
        
        if game_state.event_messages:
            log(f"Appending event messages to prompt: {game_state.event_messages}")
            prompt_text = game_state.event_messages + prompt_text
            game_state.event_messages = []
        
        response = terminal.askMenu(game_state.game_name, valid_options, promptText=prompt_text)
        log(f"User selected option: {response}")

        if response == "Buy Inventory":
            handle_buy_inventory(game_state)

        elif response == "Set Prices":
            handle_set_prices(game_state)

        elif response == "Upgrade Store":
            handle_upgrade_store(game_state)

        elif response == "View Details About Store":
            handle_print_details(game_state)

        elif response == "Continue to Next Hour":
            game_state.fast_forward = False
            in_menu = False

        elif response == "End Day (fast foward)":
            game_state.fast_forward = True
            in_menu = False

        elif response == "Talk To A Customer":
            handle_talk_customer(game_state)

        elif response == "Exit Game":
            in_menu = handle_exit(game_state)


def handle_buy_inventory(game_state):
    log("Handling buy inventory action...")
    valid_options = ["Check Inventory", "Buy an Item", "Back"]
    response = terminal.askMenu(game_state.game_name, valid_options)
    log(f"User selected: {response}")
    
    if response == "Check Inventory":
        log("User chose to check inventory.")
        summary = invLib.get_inventory_summary(game_state.store_inv)
        log(f"Inventory summary: {summary}")
        inventory_display = [
            f"Stock: {summary['stock']}/{summary['capacity']}",
            f"Free Space: {summary['free_space']}",
            f"Items in stock: {summary['items_count']}",
            ""
        ]
        log(f"Items in inventory: {summary['items']}")
        for name, count, price in summary['items']:
            inventory_display.append(f"{name} x{count} (${price:.2f} each)")
            log(f"Item: {name}, Count: {count}, Price: ${price:.2f}")
        
        terminal.drawWindowBuffered(game_state.game_name, inventory_display)
        terminal.waitUntilEnter()
        
    elif response == "Buy an Item":
        log("User chose to buy an item.")
        buyable_items = invLib.get_buyable_items(game_state)
        log(f"Buyable items: {buyable_items}")
        buyable_items.append("Back")
        log(f"Adding 'Back' option to buyable items: {buyable_items}")
        
        item_choice = terminal.askMenu(game_state.game_name, buyable_items, "What item would you like to buy?")
        log(f"User selected item: {item_choice}")
        if item_choice != "Back":
            quantity_prompt = [f"How many {item_choice} would you like to buy?", f"Cost per item: ${catalog[item_choice]['purchaseCost']:.2f}"]
            log(f"Prompting for quantity with message: {quantity_prompt}")
            try:

                quantity_str = terminal.askForInput(game_state.game_name, quantity_prompt)
                log(f"User entered quantity: {quantity_str}")
                quantity = int(quantity_str)

                
                success, cost, message = invLib.buy_item_for_inventory(game_state.store_inv, item_choice, quantity, game_state)
                log(f"Buy item result - Success: {success}, Cost: {cost}, Message: {message}")
                game_state.event_messages.append(message)
                log(f"Event messages updated: {game_state.event_messages}")
                if success:
                    log(f"Item {item_choice} purchased successfully.")
                    game_state.event_messages.append(f"Spent ${cost:.2f}")
                    
            except ValueError:
                log(f"Invalid quantity entered: {quantity_str}")
                game_state.event_messages.append("Invalid quantity entered")

def handle_set_prices(game_state):
    log("Handling set prices action...")
    summary = invLib.get_inventory_summary(game_state.store_inv)
    if not summary['items']:
        log("No items in inventory to price")
        game_state.event_messages.append("No items in inventory to price")
        return
    
    item_names = [item[0] for item in summary['items']]
    log(f"Items available for pricing: {item_names}")
    item_names.append("Back")
    log(f"Adding 'Back' option to item names: {item_names}")

    item_choice = terminal.askMenu(game_state.game_name, item_names, "Which item would you like to price?")
    log(f"User selected item for pricing: {item_choice}")
    if item_choice != "Back":
        log(f"Finding current item in inventory: {item_choice}")
        current_item = None
        for item in game_state.store_inv.listItems():
            log(f"Checking item: {item.getName()}")
            if item.getName() == item_choice:
                log(f"Found current item: {item.getName()}")
                current_item = item
                break
        
        if current_item:
            log(f"Current item found: {current_item.getName()}")
            log(f"Current price: ${current_item.getSellValue():.2f}, Purchase cost: ${current_item.getPurchaseCost():.2f}")
            price_prompt = [
                f"Current price for {item_choice}: ${current_item.getSellValue():.2f}",
                f"Purchase cost: ${current_item.getPurchaseCost():.2f}",
                "Enter new selling price:"
            ]
            try:
                log(f"Prompting for new price with message: {price_prompt}")
                new_price_str = terminal.askForInput(game_state.game_name, price_prompt)
                log(f"User entered new price: {new_price_str}")
                new_price = float(new_price_str)
                log(f"Parsed new price: {new_price}")
                if new_price > 0:
                    log(f"Setting new price for {item_choice}: ${new_price:.2f}")
                    invLib.set_item_price(game_state.store_inv, item_choice, new_price)
                    log(f"Item {item_choice} price updated successfully.")
                    game_state.event_messages.append(f"Set {item_choice} price to ${new_price:.2f}")
                else:
                    log("Price must be positive")
                    game_state.event_messages.append("Price must be positive")
            except ValueError:
                log(f"Invalid price entered: {new_price_str}")
                game_state.event_messages.append("Invalid price entered")

def handle_upgrade_store(game_state):
    log("Handling upgrade store action...")
    upgrade_options = ["Buy Storage Unit", "Upgrade Existing Storage", "Back"]
    response = terminal.askMenu(game_state.game_name, upgrade_options)
    log(f"User selected upgrade option: {response}")
    
    if response == "Buy Storage Unit":
        log("User chose to buy storage unit.")
        available_units = ["shelf", "freezer", "Back"]
        unit_choice = terminal.askMenu(game_state.game_name, available_units, "What storage would you like to buy?")
        log(f"User selected storage unit: {unit_choice}")
        
        if unit_choice != "Back":
            log(f"Checking if {unit_choice} is available for purchase")
            cost = storageLib.units[unit_choice]['purchaseCost']
            log(f"Cost for {unit_choice}: ${cost:.2f}")
            if game_state.store_balance >= cost:
                log(f"User has enough balance to buy {unit_choice}")
                new_unit = storageLib.StorageUnit(unit_choice)
                log(f"Creating new storage unit: {new_unit}")
                success = game_state.store_inv.addStorageUnit(new_unit)
                log(f"Adding storage unit result: {success}")
                if success:
                    log(f"Storage unit {unit_choice} added successfully.")
                    log(f"Deducting cost from store balance: ${cost:.2f}")
                    game_state.store_balance -= cost
                    log(f"New store balance: ${game_state.store_balance:.2f}")
                    game_state.event_messages.append(f"Bought {unit_choice} for ${cost}")
                    
                else:
                    game_state.event_messages.append("Cannot add this storage unit")
                    log(f"Failed to add storage unit {unit_choice}.")
            else:
                game_state.event_messages.append("Not enough money")
                log(f"User does not have enough money to buy {unit_choice}.")

def handle_print_details(game_state):
    log("Handling print details action...")
    summary = invLib.get_inventory_summary(game_state.store_inv)
    log(f"Inventory summary for details: {summary}")
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
        log(f"Item: {name}, Count: {count}, Price: ${price:.2f}")
        profit_margin = ((price - catalog[name]['purchaseCost']) / catalog[name]['purchaseCost']) * 100
        log(f"Profit margin for {name}: {profit_margin:.1f}%")
        details.append(f"  {name}: {count}x @ ${price:.2f} ({profit_margin:.1f}% markup)")

    
    if game_state.store_inv.getStorageUnits():
        log("User has storage units:")
        details.append("")

        details.append("Storage Units:")
        log(f"Storage units in inventory: {game_state.store_inv.getStorageUnits()}")
        for unit in game_state.store_inv.getStorageUnits():
            log(f"  {unit}")
            details.append(f"  {unit}")
    
    terminal.drawWindowBuffered(game_state.game_name, details)
    terminal.waitUntilEnter()

def handle_talk_customer(game_state):
    log("Handling talk to customer action...")
    
    # Check if there's a customer at the current tick
    tick_index = game_state.store_tick_count - 1
    if tick_index < 0 or tick_index >= len(game_state.customer_distribution):
        log("No customer to talk to at current tick")
        game_state.event_messages.append("No customers are currently in the store")
        return
    
    current_customer = game_state.customer_distribution[tick_index]
    
    if current_customer is None:
        log("No customer at current tick")
        game_state.event_messages.append("No customers are currently in the store")
        return
    
    # Handle multiple customers
    if isinstance(current_customer, list):
        log(f"Multiple customers present: {current_customer}")
        customer_options = []
        for i, customer in enumerate(current_customer):
            customer_options.append(f"Customer {i+1} (Budget: ${customer.budget:.2f}, Preferences: {', '.join(customer.preferences)})")
        customer_options.append("Back")
        
        choice = terminal.askMenu(game_state.game_name, customer_options, "Which customer would you like to talk to?")
        if choice == "Back":
            return
        
        # Get selected customer index
        selected_index = customer_options.index(choice)
        selected_customer = current_customer[selected_index]
    
    # Handle single customer
    elif isinstance(current_customer, customerLib.Customer):
        log(f"Single customer present: {current_customer}")
        selected_customer = current_customer
    
    else:
        log("Invalid customer type")
        game_state.event_messages.append("Error: Unable to communicate with customer")
        return
    
    # Generate dialogue using the customer dialogue library
    try:
        import customerDialogueLib
        log("Generating customer dialogue...")
        
        # Create a context-aware prompt based on customer preferences and budget
        customer_context = f"You are a customer in a store with a budget of ${selected_customer.budget:.2f}. You are interested in {', '.join(selected_customer.preferences)} items. "
        
        # Show customer dialogue
        dialogue_options = ["Ask about preferences", "Ask about budget", "Recommend items", "Generate AI dialogue", "Back"]
        
        while True:
            choice = terminal.askMenu(game_state.game_name, dialogue_options, f"Talking to customer (Budget: ${selected_customer.budget:.2f})")
            
            if choice == "Ask about preferences":
                preferences_text = f"Customer says: 'I'm looking for {', '.join(selected_customer.preferences)} items today.'"
                terminal.drawWindowBuffered(game_state.game_name, [preferences_text, "", "Press Enter to continue..."])
                terminal.waitUntilEnter()
                
            elif choice == "Ask about budget":
                budget_text = f"Customer says: 'I have about ${selected_customer.budget:.2f} to spend today.'"
                terminal.drawWindowBuffered(game_state.game_name, [budget_text, "", "Press Enter to continue..."])
                terminal.waitUntilEnter()
                
            elif choice == "Recommend items":
                # Get items that match customer preferences
                compatible_items = invLib.get_customer_compatible_items(game_state.store_inv, selected_customer.preferences)
                affordable_items = [item for item in compatible_items if item['price'] <= selected_customer.budget]
                
                if affordable_items:
                    recommendation_text = [
                        "You recommend:",
                        ""
                    ]
                    for item in affordable_items[:3]:  # Show top 3 recommendations
                        recommendation_text.append(f"- {item['name']}: ${item['price']:.2f} ({item['category']})")
                    
                    if len(affordable_items) > 0:
                        # Slightly increase customer satisfaction for good service
                        selected_customer.satisfaction = min(1.0, selected_customer.satisfaction + 0.1)
                        recommendation_text.append("")
                        recommendation_text.append("Customer seems pleased with your recommendations!")
                else:
                    recommendation_text = [
                        "Unfortunately, we don't have any items that match",
                        "your preferences within your budget right now.",
                        "",
                        "Customer looks disappointed..."
                    ]
                    # Slightly decrease satisfaction
                    selected_customer.satisfaction = max(0.0, selected_customer.satisfaction - 0.05)
                
                recommendation_text.append("")
                recommendation_text.append("Press Enter to continue...")
                terminal.drawWindowBuffered(game_state.game_name, recommendation_text)
                terminal.waitUntilEnter()
                
            elif choice == "Generate AI dialogue":
                try:
                    ai_dialogue = customerDialogueLib.generate_customer_text(game_state, selected_customer)
                    dialogue_display = [
                        "AI-Generated Customer Response:",
                        ""]
                    dialogue_display.extend(ai_dialogue)
                    dialogue_display.extend([
                        "",
                        "Press Enter to continue..."
                    ])
                    terminal.drawWindowBuffered(game_state.game_name, dialogue_display)
                    terminal.waitUntilEnter()
                except Exception as e:
                    log(f"Error generating AI dialogue: {e}")
                    error_display = [
                        "Sorry, AI dialogue is not available right now.",
                        "Make sure Ollama is installed and running.",
                        "",
                        "Press Enter to continue..."
                    ]
                    terminal.drawWindowBuffered(game_state.game_name, error_display)
                    terminal.waitUntilEnter()
                
            elif choice == "Back":
                break
        
        game_state.event_messages.append(f"You talked to a customer (Budget: ${selected_customer.budget:.2f})")
        log("Customer conversation completed")
        

    except ImportError:
        log("customerDialogueLib not available")
        # Fallback simple dialogue
        simple_dialogue = [
            f"Customer says: 'Hello! I'm looking for {', '.join(selected_customer.preferences)} items.'",
            f"'I have ${selected_customer.budget:.2f} to spend today.'",
            "",
            "Press Enter to continue..."
        ]
        terminal.drawWindowBuffered(game_state.game_name, simple_dialogue)
        terminal.waitUntilEnter()
        game_state.event_messages.append("You talked to a customer")

def handle_exit(game_state):
    log("Handling exit action...")
    valid_choices = ["Yes", "No"]
    message = ["Are you sure you want to exit?", "The game does not save data"]
    response = terminal.askMenu(game_state.game_name, valid_choices, message)
    log(f"User response to exit confirmation: {response}")
    if response == "Yes":
        log("Exiting game...")
        game_state.game_is_running = False
        return False
    return True


def do_customer_shopping(game_state):
    log("Handling customer shopping...")
    log(f"Current tick count: {game_state.store_tick_count}")
    tick_index = game_state.store_tick_count - 1
    log(f"Current tick index: {tick_index}")
    
    if tick_index >= len(game_state.customer_distribution):
        log(f"Tick index {tick_index} is out of bounds for customer distribution.")
        log(f"Tick {tick_index}: No customer in distribution.")
        return
        
    game_state.current_tick_customer = game_state.customer_distribution[tick_index]
    log(f"Current tick customer: {game_state.current_tick_customer}")
    
    if isinstance(game_state.current_tick_customer, customerLib.Customer):
        log(f"Tick {tick_index}: Single customer detected: {game_state.current_tick_customer}")
        customer = game_state.current_tick_customer
        log(f"Tick {tick_index}: Customer {customer} with budget {getattr(customer, 'budget', None)} and preferences {getattr(customer, 'preferences', None)}")
        compatible_items = invLib.get_customer_compatible_items(game_state.store_inv, None)#customer.preferences)
        log(f"Tick {tick_index}: Compatible items: {compatible_items}")
        
        total_spent = 0
        items_bought = []
        
        # https://stackoverflow.com/questions/16310015/what-does-this-mean-key-lambda-x-x1
        compatible_items.sort(key=lambda x: x['price'])
        log(f"Tick {tick_index}: Sorted compatible items by price: {compatible_items}")
        
        for item_data in compatible_items:
            log(f"Tick {tick_index}: Trying to sell {item_data['name']} (price: {item_data['price']}, stock: {item_data['stock']}) to customer with budget {getattr(customer, 'budget', None)}")
            if customer.budget >= item_data['price'] and item_data['stock'] > 0:
                log(f"Tick {tick_index}: Customer can afford {item_data['name']}, attempting to sell...")
                success, revenue, message = invLib.sell_item_from_inventory(
                    game_state.store_inv, 
                    item_data['name'], 
                    1, 
                    customer.budget
                )
                log(f"Tick {tick_index}: Sell result: success={success}, revenue={revenue}, message={message}")
                if success:
                    log(f"Tick {tick_index}: Successfully sold {item_data['name']} to customer.")   
                    customer.budget -= revenue
                    total_spent += revenue
                    game_state.store_balance += revenue
                    items_bought.append(item_data['name'])
                    log(f"Tick {tick_index}: Customer bought {item_data['name']}, remaining budget: {customer.budget:.2f}")
        
        if items_bought:
            
            game_state.event_messages.append(f"Customer bought: {', '.join(items_bought)} (${total_spent:.2f})")
            log(f"Tick {tick_index}: Customer bought: {', '.join(items_bought)} (${total_spent:.2f})")
        else:
            game_state.event_messages.append("Customer left without buying anything")
            log(f"Tick {tick_index}: Customer left without buying anything")
        
    elif isinstance(game_state.current_tick_customer, list):
        
        log(f"Tick {tick_index}: Multiple customers in group: {game_state.current_tick_customer}")
        for customer in game_state.current_tick_customer:
            log(f"Tick {tick_index}: Processing customer: {customer}")
            # Process each customer in the group
            # (recursively call with single customer)
            log(f"Tick {tick_index}: Creating temporary state for customer: {customer}")
            # Create a temporary state to avoid modifying the main game state
            temp_state = type('temp', (), {})()
            temp_state.store_inv = game_state.store_inv
            temp_state.store_balance = game_state.store_balance
            temp_state.event_messages = []
            temp_state.current_tick_customer = customer
            temp_state.store_tick_count = game_state.store_tick_count
            temp_state.customer_distribution = [customer]
            log(f"Tick {tick_index}: Handling shopping for customer: {customer}")

            log(f"Tick {tick_index}: Customer budget: {getattr(customer, 'budget', None)}, preferences: {getattr(customer, 'preferences', None)}")
            do_customer_shopping(temp_state)
            log(f"Tick {tick_index}: Shopping completed for customer: {customer}")
            game_state.store_balance = temp_state.store_balance
            game_state.event_messages.extend(temp_state.event_messages)
            log(f"Tick {tick_index}: Updated store balance: {game_state.store_balance}, event messages: {game_state.event_messages}")

# game phases
def start_day(game_state):
    log("Starting a new day...")
    # generate customers for the day
    customers = customerLib.spawn_customers(game_state.store_day, game_state.store_rating, game_state.store_difficulty)
    log(f"Generated {len(customers)} customers for day {game_state.store_day} with rating {game_state.store_rating} and difficulty {game_state.store_difficulty}")
    # generate customer shopping distribution
    game_state.customer_distribution = customerLib.get_customer_shop_distribution(customers, game_state.store_ticks_per_day)
    log(f"Generated customer shopping distribution for day {game_state.store_day}: {game_state.customer_distribution}")

    # print opening summary
    log("Printing opening summary...")
    print_opening_summary(game_state)

    # let user do actions
    log(f"Entering tick menu... with tick count {game_state.store_tick_count}")
    do_tick_menu(game_state)

def handle_shopping_phase(game_state):
    log(f"Handling shopping phase for tick {game_state.store_tick_count}...")
    if game_state.fast_forward == True:
        log("Fast forwarding through shopping phase...")
        while game_state.store_tick_count <= game_state.store_ticks_per_day:
            log(f"Tick {game_state.store_tick_count}: Fast forwarding shopping...")
            log(f"Current customer for tick {game_state.store_tick_count}: {game_state.customer_distribution[game_state.store_tick_count - 1]}")
            do_customer_shopping(game_state)
            game_state.store_tick_count += 1
        log("Fast forward complete, resetting fast forward flag.")
        game_state.fast_forward = False
    else:
        log(f"Handling shopping for tick {game_state.store_tick_count}...")
        log(f"Current customer for tick {game_state.store_tick_count}: {game_state.customer_distribution[game_state.store_tick_count - 1]}")
        do_customer_shopping(game_state)
        do_tick_menu(game_state)
        game_state.store_tick_count += 1

def end_day(game_state):
    log("Ending the day...")
    print_closing_summary(game_state)
    log(f"Ending day {game_state.store_day}...")
    game_state.store_tick_count = 0
    game_state.store_day += 1
    game_state.event_messages = []

def main():
    log("main(): running check_platform()")
    check_platform()
    log("main(): running terminal.format.hideCursor()")
    terminal.format.hideCursor()
    log("main(): running game_state = GameState()")
    game_state = GameState()

    log("main(): running starting_menu(game_state)")
    starting_menu(game_state)
    log("main(): running ask_difficulty(game_state)")
    ask_difficulty(game_state)
    log("main(): running get_store_name(game_state)")
    get_store_name(game_state)
    log("main(): running game_state.store_inv = starter_inventory(game_state)")
    game_state.store_inv = starter_inventory(game_state)

    # game loop
    log("main(): Starting game loop...")
    while game_state.game_is_running:
        log(f"main(): Game loop iteration with tick count {game_state.store_tick_count}")
        if game_state.store_tick_count == 0:
            log("main(): Tick count is 0, starting a new day...")
            start_day(game_state)
            log("main(): New day started. Adding 1 to store tick count.")
            game_state.store_tick_count += 1
        elif game_state.store_tick_count >= 1 and game_state.store_tick_count <= game_state.store_ticks_per_day:
            log(f"main(): tick count {game_state.store_tick_count} is in shopping phase, handling shopping...")
            handle_shopping_phase(game_state)
        elif game_state.store_tick_count == (game_state.store_ticks_per_day + 1):
            log(f"main(): tick count {game_state.store_tick_count} is at end of day, ending day...")
            import matrixLib
            matrixLib.continueAnim(True)
            # https://www.stratascratch.com/blog/python-threading-like-a-pro/#:~:text=Thread()%20function%20creates%20a,thread%2C%20which%20begins%20its%20execution.
            import threading
            import time
            animation = threading.Thread(target=matrixLib.animate)
            animation.daemon = True
            animation.start()
            time.sleep(4.5)
            matrixLib.continueAnim(False)
            time.sleep(0.25)
            
            terminal.clearV2()

            end_day(game_state)
            
        else:
            log(f"main(): Unknown tick count {game_state.store_tick_count}, raising exception.")
            raise Exception(f"Unknown error: {game_state.store_tick_count} is not in range 0-{game_state.store_ticks_per_day}")
    
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    main()