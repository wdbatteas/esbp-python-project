
import ollama


def generate_customer_text():
    """
    Generate a fictional customer description using an Ollama language model.
    Returns a string with customer details.
    """


    # The prompt we send to the language model
    prompt = "Speak as if you are a customer in a store. Describe your preferences, budget, and what you are looking for. Keep the talk very short and concise, like a real customer would. " \


    # Call the local Ollama model. Change 'mistral' to whatever model you have (e.g., 'llama3', 'phi3')
    response = ollama.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': prompt}
    ])


    # Extract and return the generated text
    customer_text = response['message']['content']
    return customer_text




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



