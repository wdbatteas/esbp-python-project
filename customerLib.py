# Member R

import random

class Customer:
    def __init__(self, budget: float, preferences: list[str]):
        self.budget = budget
        self.preferences = preferences  # e.g., ['food', 'dairy']
        self.satisfaction = 1.0


    def __repr__(self):
        return f"<Customer ${self.budget:.2f}, prefs={self.preferences}, satisfaction={self.satisfaction:.2f}>"


def spawn_customers(day_number: int, store_rating: float, difficulty: str = "medium") -> list[Customer]:
    num_customers = 5 + day_number
    customers = []
    categories_pool = ['food', 'dairy', 'tech', 'clothing', 'toys', 'books']


    # Difficulty settings
    if difficulty == "Easy":
        min_budget, max_budget = 40, 70
        min_prefs, max_prefs = 1, 2
    elif difficulty == "Medium":
        min_budget, max_budget = 25, 50
        min_prefs, max_prefs = 2, 3
    elif difficulty == "Hard":
        min_budget, max_budget = 15, 35
        min_prefs, max_prefs = 3, 5
    elif difficulty == "Insane":
        min_budget, max_budget = 5, 20
        min_prefs, max_prefs = 4, 6
    else:
        # fallback to medium if insane not enabled or invalid
        min_budget, max_budget = 25, 50
        min_prefs, max_prefs = 2, 3


    for _ in range(num_customers):
        budget = round(random.uniform(min_budget, max_budget) + store_rating * 2, 2)
        num_prefs = random.randint(min_prefs, max_prefs)
        preferences = random.sample(categories_pool, min(num_prefs, len(categories_pool)))
        customers.append(Customer(budget, preferences))


    return customers


def customer_shops(customer_obj, inventory_obj):
    catalog = inventory_obj.get_public_catalog()
    spent = 0.0
    starting_budget = customer_obj.budget
    purchased_any = False


    for item in catalog:
        if item['category'] in customer_obj.preferences and item['price'] <= customer_obj.budget:
            success = inventory_obj.purchase_item(item['name'])
            if success:
                customer_obj.budget -= item['price']
                spent += item['price']
                purchased_any = True
            else:
                customer_obj.satisfaction -= 0.1  # penalize for stock-out


    if not purchased_any:
        customer_obj.satisfaction -= 0.2  # penalty for walking out empty


    customer_obj.satisfaction = max(0, min(customer_obj.satisfaction, 1))  # clamp 0–1


    return {
        'spent': round(spent, 2),
        'satisfaction_score': round(customer_obj.satisfaction, 2),
        'budget_remaining': round(customer_obj.budget, 2),
	}

def get_customer_shop_distribution(customers, max_ticks_per_day):
   
#Distributes customers randomly across ticks in a day.
#Returns a list of length max_ticks_per_day, with each slot containing either a Customer or None
#If there are more customers than ticks, some ticks may have multiple customers (as a list)

    dist = [None for _ in range(max_ticks_per_day)]
    for customer in customers:
        tick = random.randint(0, max_ticks_per_day - 1)
        if dist[tick] is None:
            dist[tick] = customer
        else:
            # If a tick already has a customer, make it a list
            if isinstance(dist[tick], list):
                dist[tick].append(customer)
            else:
                dist[tick] = [dist[tick], customer]
    return dist
