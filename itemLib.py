"""
    Items were generated using the following prompt in Copilot:
        "expand this dictionary to contain as many items as you can think of that are commonly found in a store. include produce, bakery, anything in freezers/refrigerators, maybe canned goods, snacks, possibly even appliances, clothes, cleaning supplies, electronics, videogames, and anythign else that makes sense
        catalog = { 'Apple': { 'purchaseCost': 2, 'type': 'fruit', } }
        you do not need to change the purchaseCost value, keep it at 2 for all items so that we can change them later. though still try to reasonably organize items by category using their 'type' field. make the groupings broad"
"""


catalog = {
    # Produce
    'Apple': {'purchaseCost': 2, 'type': 'fruit'},
    'Banana': {'purchaseCost': 2, 'type': 'fruit'},
    'Orange': {'purchaseCost': 2, 'type': 'fruit'},
    'Grapes': {'purchaseCost': 2, 'type': 'fruit'},
    'Carrot': {'purchaseCost': 2, 'type': 'vegetable'},
    'Lettuce': {'purchaseCost': 2, 'type': 'vegetable'},
    'Tomato': {'purchaseCost': 2, 'type': 'vegetable'},
    'Potato': {'purchaseCost': 2, 'type': 'vegetable'},
    'Broccoli': {'purchaseCost': 2, 'type': 'vegetable'},


    # Bakery
    'Bread': {'purchaseCost': 2, 'type': 'bakery'},
    'Croissant': {'purchaseCost': 2, 'type': 'bakery'},
    'Bagel': {'purchaseCost': 2, 'type': 'bakery'},
    'Muffin': {'purchaseCost': 2, 'type': 'bakery'},
    'Donut': {'purchaseCost': 2, 'type': 'bakery'},


    # # Frozen/Refrigerated
    # 'Milk': {'purchaseCost': 2, 'type': 'dairy'},
    # 'Eggs': {'purchaseCost': 2, 'type': 'dairy'},
    # 'Cheese': {'purchaseCost': 2, 'type': 'dairy'},
    # 'Yogurt': {'purchaseCost': 2, 'type': 'dairy'},
    # 'Ice Cream': {'purchaseCost': 2, 'type': 'frozen'},
    # 'Frozen Pizza': {'purchaseCost': 2, 'type': 'frozen'},
    # 'Frozen Vegetables': {'purchaseCost': 2, 'type': 'frozen'},


    # # Canned Goods
    # 'Canned Corn': {'purchaseCost': 2, 'type': 'canned'},
    # 'Canned Beans': {'purchaseCost': 2, 'type': 'canned'},
    # 'Canned Soup': {'purchaseCost': 2, 'type': 'canned'},
    # 'Canned Tuna': {'purchaseCost': 2, 'type': 'canned'},


    # # Snacks
    # 'Chocolate Bar': {'purchaseCost': 2, 'type': 'snack'},
    # 'Potato Chips': {'purchaseCost': 2, 'type': 'snack'},
    # 'Granola Bar': {'purchaseCost': 2, 'type': 'snack'},
    # 'Popcorn': {'purchaseCost': 2, 'type': 'snack'},
    # 'Cookies': {'purchaseCost': 2, 'type': 'snack'},


    # # Cleaning Supplies
    # 'Dish Soap': {'purchaseCost': 2, 'type': 'cleaning'},
    # 'Laundry Detergent': {'purchaseCost': 2, 'type': 'cleaning'},
    # 'Bleach': {'purchaseCost': 2, 'type': 'cleaning'},
    # 'Glass Cleaner': {'purchaseCost': 2, 'type': 'cleaning'},


    # # Clothes
    # 'T-Shirt': {'purchaseCost': 2, 'type': 'clothing'},
    # 'Jeans': {'purchaseCost': 2, 'type': 'clothing'},
    # 'Jacket': {'purchaseCost': 2, 'type': 'clothing'},
    # 'Sneakers': {'purchaseCost': 2, 'type': 'clothing'},
    # 'Shoes': {'purchaseCost': 2, 'type': 'clothing'},


    # # Electronics
    # 'Headphones': {'purchaseCost': 2, 'type': 'electronics'},
    # 'Phone Charger': {'purchaseCost': 2, 'type': 'electronics'},
    # 'Bluetooth Speaker': {'purchaseCost': 2, 'type': 'electronics'},
    # 'Laptop': {'purchaseCost': 2, 'type': 'electronics'},


    # # Video Games
    # 'Game Console': {'purchaseCost': 2, 'type': 'gaming'},
    # 'Controller': {'purchaseCost': 2, 'type': 'gaming'},
    # 'Video Game': {'purchaseCost': 2, 'type': 'gaming'},


    # # Appliances
    # 'Microwave': {'purchaseCost': 2, 'type': 'appliance'},
    # 'Toaster': {'purchaseCost': 2, 'type': 'appliance'},
    # 'Blender': {'purchaseCost': 2, 'type': 'appliance'},
    # 'Coffee Maker': {'purchaseCost': 2, 'type': 'appliance'}
}
def getItemsFromCategory(cat: str) -> list[str]:
    keys = list(catalog.keys())
    result = []
    for key in keys:
        typ = catalog[key]['type']
        if cat == typ:
            result.append(key)
    return result

def getItemCost(itemName: str, itemCount: int=1):
    return catalog[itemName]['purchaseCost'] * itemCount


class Item:
    def __init__(self, name: str, count:int=1):
        self.name = name
        self.count = count
        self.type = catalog[name]['type']
        self.sellValue = catalog[name]['purchaseCost']
        self.purchaseCost = catalog[name]['purchaseCost']


    def getName(self) -> str:
        return self.name
    def getCount(self) -> int:
        return self.count
    def getSellValue(self) -> float:
        return self.sellValue
    def getItemCategory(self) -> str:
        return self.type
    def getPurchaseCost(self) -> float:
        return self.purchaseCost
    def getMarkup(self) -> float:
        """
        Returns the price markup of the item (sell price - base cost) / base cost
        """
        purchase_cost = self.getPurchaseCost()
        sell_value = self.getSellValue()
       
        return (sell_value - purchase_cost) / purchase_cost
   
    def setCount(self, count:int):
        self.count = count
    def setSellValue(self, sellValue:float):
        self.sellValue = sellValue
    def addCount(self, count:int):
        self.count += count
    def __str__(self):
        return str(self.getName()+" x"+str(self.getCount())+" ($"+str(self.getSellValue())+" per, worth: $"+str(self.getSellValue()*self.getCount())+")")
   


   




