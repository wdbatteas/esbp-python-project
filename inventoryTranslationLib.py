from inventoryLib import Inventory
from itemLib import Item, catalog
from storageLib import StorageUnit

def create_starter_inventory(difficulty):
    """Creates a basic starting inventory with shelf storage"""
    inv = Inventory()
    
    # Add basic storage unit
    shelf = StorageUnit("shelf")
    inv.addAvailableStorage('shelf')
    inv.addStorageUnit(shelf)
    
    # Add some starter items to available list
    starter_categories = ['fruit', 'vegetable', 'dairy', 'bakery', 'snack']
    for category in starter_categories:
        inv.addAvailableItem(category)
    
    return inv

def get_buyable_items():
    """Returns list of all items available for purchase"""
    return list(catalog.keys())

def get_items_by_category(category):
    """Returns items matching a specific category"""
    items = []
    for item_name, item_data in catalog.items():
        if item_data['type'] == category:
            items.append(item_name)
    return items

def get_inventory_summary(inventory):
    """Returns formatted inventory status"""
    stock = inventory.getTotalStock()
    capacity = inventory.getCapacity()
    items = inventory.listItems()
    
    summary = {
        'stock': stock,
        'capacity': capacity,
        'free_space': capacity - stock,
        'items_count': len(items),
        'items': [(item.getName(), item.getCount(), item.getSellValue()) for item in items]
    }
    return summary

def buy_item_for_inventory(inventory, item_name, quantity, game_state):
    """Attempts to buy items for inventory, returns success and cost"""
    if item_name not in catalog:
        return False, 0, "Item not found"
    
    cost_per_item = catalog[item_name]['purchaseCost']
    total_cost = cost_per_item * quantity
    
    # Check if player has enough money
    if game_state.store_balance < total_cost:
        return False, 0, "Not enough money"
    
    # Try to add to inventory
    success = inventory.addStock(item_name, quantity)
    if success:
        game_state.store_balance -= total_cost
        return True, total_cost, f"Purchased {quantity}x {item_name}"
    else:
        return False, 0, "Not enough inventory space or item not allowed"

def sell_item_from_inventory(inventory, item_name, quantity, customer_budget):
    """Attempts to sell item to customer, returns success and revenue"""
    if not inventory.hasItem(item_name, quantity):
        return False, 0, "Not enough stock"
    
    # Find the item to get sell price
    for item in inventory.listItems():
        if item.getName() == item_name:
            sell_price = item.getSellValue()
            total_cost = sell_price * quantity
            
            if customer_budget >= total_cost:
                success = inventory.removeItem(item_name, quantity)
                if success:
                    return True, total_cost, f"Sold {quantity}x {item_name}"
            else:
                return False, 0, "Customer can't afford item"
    
    return False, 0, "Item not found"

def set_item_price(inventory, item_name, new_price):
    """Sets selling price for an item in inventory"""
    for item in inventory.listItems():
        if item.getName() == item_name:
            item.setSellValue(new_price)
            return True
    return False

def get_customer_compatible_items(inventory, customer_preferences):
    """Returns items customer might want based on preferences"""
    compatible_items = []
    for item in inventory.listItems():
        if item.getItemCategory() in customer_preferences and item.getCount() > 0:
            compatible_items.append({
                'name': item.getName(),
                'category': item.getItemCategory(),
                'price': item.getSellValue(),
                'stock': item.getCount()
            })
    return compatible_items