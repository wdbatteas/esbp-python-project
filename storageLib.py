from itemLib import Item
from itemLib import catalog


units = {
    'shelf': {
        'purchaseCost': 2,
        'capacity': 20,
        'holds': ['fruit', 'vegetable', 'bakery', 'canned', 'snack', 'clothing', 'cleaning'],
        'powerRating': 0
    },
    'freezer': {
        'purchaseCost': 2,
        'capacity': 20,
        'holds': ['dairy'],
        'powerRating': 10
    }
}


class StorageUnit:


    """
    StorageUnits increase your storage space when added to your store, allowing you to sell more items at once. They do not directly store items, but instead increase the storage cap
    Each storage unit has a power rating as well
    """


    def __init__(self, name: str, count: int=1):
        name = name.lower()
        self.name = name
        self.count = count
        self.itemCategories = units[name]['holds']
        self.capacity = units[name]['capacity']
        self.powerRating = units[name]['powerRating']


    def getName(self) -> str:
        return self.name
    def getMaxItems(self) -> int:
        return self.capacity
    def getItemCategories(self) -> str:
        return self.itemCategories
    def canHoldCategory(self, category=str) -> bool:
        return self.getItemCategories().__contains__(category)
    def getPowerRating(self) -> int:
        return self.powerRating
    def getCount(self) -> int:
        return self.count
    def getCapacity(self) -> int:
        return self.capacity * self.getCount()
   
    def rename(self, newName):
        self.name = newName
    def setCapacity(self, newCapacity: int):
        self.capacity = newCapacity
    def setPowerRating(self, newPowerRating: int):
        self.powerRating = newPowerRating
    def addCount(self, newCount: int):
        self.count += newCount


    def __str__(self):
        name = self.getName()
        count = self.getCount()
        cat = ", ".join(self.getItemCategories())
        cap = self.getCapacity()
        power = self.getPowerRating()


        return f"{name} x{count} [Holds: {cat}] | [Capacity: {cap}] | [Power Rating: {power}]"
   
freeze = StorageUnit("shelf")
print(freeze)


   



