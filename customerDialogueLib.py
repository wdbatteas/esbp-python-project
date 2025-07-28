
import ollama
from terminalLib import log, color
import random
from inventoryTranslationLib import get_inventory_summary

def generate_customer_text(game=None, customer=None):
    """
    Generate a fictional customer description using an Ollama language model.
    Returns a string with customer details.
    """
    
    customer_behaviors = {
        "impatient": "You are very impatient and want everything done quickly.",
        "chatty": "You love to talk and share stories with the staff.",
        "indecisive": "You can't make up your mind and keep changing what you want.",
        "bargain_hunter": "You are always looking for discounts and deals.",
        "complainer": "You tend to complain about products and prices.",
        "excited": "You are overly excited about shopping.",
        "confused": "You are confused about what you want or need.",
        "distracted": "You get distracted easily and lose focus on shopping.",
        "rude": "You are rude and short-tempered with staff.",
        "friendly": "You are very friendly and polite.",
        "inspector": "You are the story inspector. You have details about the store. You criticize everything about the store."
    }
        
    
    behavior_key = random.choice(list(customer_behaviors.keys()))
    behavior_description = customer_behaviors[behavior_key]
    
    # The prompt we send to the language model
    prompt = "To format: please use only these escape characters: \033[1m for bold, \033[0m to reset, \033[91m for color RED, \033[92m for color GREEN. Do not ever use **bold** or <font>html</font> as they wont work. Make sure to use these formatting at least once.\n"
    prompt += "This is your behaviour:"
    prompt += behavior_description
    
    if behavior_key == "inspector":
        prompt += f"\nGame Details: {vars(game)}\n"
        
         # Add inventory summary here
        if hasattr(game, "store_inv") and game.store_inv is not None:
            summary = get_inventory_summary(game.store_inv)
            inventory_lines = [
                f"Stock: {summary['stock']}/{summary['capacity']}",
                f"Free Space: {summary['free_space']}",
                f"Items in stock: {summary['items_count']}",
            ]
            for name, count, price in summary['items']:
                inventory_lines.append(f"{name} x{count} (${price:.2f} each)")
            prompt += "Inventory Details:\n" + "\n".join(inventory_lines) + "\n"
        else:
            prompt += "Inventory Details: (No inventory found)\n"
    else:
        prompt += "You are a customer."


    if customer:
        prompt += f"Details about you: {customer}"

    log("Logging prmopt")
    log(prompt)

    # Call the local Ollama model. Change 'mistral' to whatever model you have (e.g., 'llama3', 'phi3')
    response = ollama.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    


    # Extract and return the generated text
    customer_text = response['message']['content']

    log("logging response")
    log(customer_text)

    # break into sentences if over 80 characters
    # break into words and check if combination is over 80 words
    # break into words

    # break into lines with max 80 characters
    words = customer_text.split()
    lines = []
    if behavior_key == "inspector":
        lines.append(f"{color.BRIGHT_GREEN} THE INPECTOR HAS ARRIVED {color.RESET}")
    current_line = ""
    
    for word in words:
        # check if adding this word would exceed 80 characters
        if len(current_line + " " + word) <= 80:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            # add current line to lines and start a new line
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)

    
    
    return lines




def use_customer(customer_text):
    """
    Simulate using the generated customer text in another function.
    For now, it just prints it nicely.
    """
    print("\n-------------------------------------------")
    print(customer_text)
    print("-------------------------------------------\n")


    # You can later parse this and use it for simulation, storing to file, etc.








#Do not use this part this is for testing purposes only
def main():
    """
    Main function to generate a customer and use it.
    """
    # Generate customer text using Ollama
    customer_description = generate_customer_text()


    # Use the generated text in other parts of the program
    use_customer(customer_description)




# Do not use this part this is for testing purposes only
if __name__ == "__main__":
    main()



