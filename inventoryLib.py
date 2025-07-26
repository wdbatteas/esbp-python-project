from itemLib import Item
from storageLib import StorageUnit


class Inventory:
    def __init__(
        self,
        maxCapacity: int = 0,
        items: list[Item] = [],
        availableItems: list[str] = [],
        availableStorageUnits: list[str] = [],
        storageUnits: list[StorageUnit] = []
    ):
        # ItemStorage variables
        self.inventory = items.copy()
        self.capacity = maxCapacity
        self.availableItems = availableItems.copy()
        # Inventory variables
        self.availableStorageUnits = availableStorageUnits.copy()
        self.storage = storageUnits.copy()


    # --- ItemStorage methods ---


    def getTotalStock(self) -> int:
        # Sums up the count of all items in inventory
        sum = 0
        for item in self.listItems():
            sum += item.getCount()
        return sum


    def getCapacity(self) -> int:
        # Returns the current max capacity of the inventory
        return self.capacity


    def getAvailableItems(self) -> list[str]:
        # Returns a list of item names that can be stored
        return self.availableItems


    def hasAvailableItem(self, item: str) -> bool:
        # Checks if an item name is in the available items list
        return self.getAvailableItems().__contains__(item)


    def listItems(self, minStock: int=1) -> list[Item]:
        # Returns all items in inventory (ignores minStock param)
        return self.inventory


    def listStorage(self) -> list[int]:
        # Returns [free space, used space] in inventory
        stock = self.getTotalStock()
        cap = self.getCapacity()
        free = cap - stock
        return [free, stock]


    def getItemsOfCategory(self, category=str) -> list[Item]:
        # Returns all items matching a given category
        items = []
        for item in self.listItems():
            if item.getItemCategory() == category:
                items.append(item)
        return items


    def addAvailableItem(self, newItem=str):
        # Adds a new item name to the available items list
        self.availableItems.append(newItem)


    def hasItem(self, itemName: str, count:int=1) -> bool:
        # Checks if inventory contains at least 'count' of itemName
        for item in self.inventory:
            if item == None:
                break
            if item.getName() == itemName:
                itemCount = item.getCount()
                if itemCount >= count:
                    return True
        return False


    def addCapacity(self, extra:int):
        # Increases the inventory's max capacity by 'extra'
        self.capacity += extra


    def addStock(self, item, count: int=1) -> bool:
        # Adds stock for an item (by Item object or name)
        typ = type(item)
        if typ == Item:
            # If item is an Item object, get its name and count
            itemName = item.getName()
            count = item.getCount()
        if typ == str:
            # If item is a string, create a new Item object
            itemName = item
            item = Item(itemName, count)
        # Check if adding would exceed capacity
        if self.getTotalStock() + count > self.getCapacity():
            return False
        # Check if item is allowed in inventory
        if (not self.hasAvailableItem(itemName)) & (not self.hasAvailableItem(item.getItemCategory())):
            return False
        # Try to find existing item and add count
        for i in range(len(self.inventory)):
            if self.inventory[i] != None:
                if itemName == self.inventory[i].getName():
                    self.inventory[i].addCount(count)
                    return True
        # If not found, append new item
        self.inventory.append(item)
        return True


    def removeItem(self, itemName:str, amt:int=1) -> bool:
        # Removes 'amt' count from itemName, removes item if count <= 0
        index = 0
        item_Deducted = False
        for itemCheck in self.inventory:
            if itemCheck == None:
                break
            if itemCheck.getName() == itemName:
                count = itemCheck.getCount()
                count -= amt
                self.inventory[index].setCount(count)
                if count <= 0:
                    self.inventory.remove(self.inventory[index])
                item_Deducted = True
                break
            index += 1
        if item_Deducted == False:
            return False
        return True


    # --- Inventory methods ---


    def getStorageUnits(self) -> list[StorageUnit]:
        # Returns all storage units in inventory
        return self.storage


    def getItemInventory(self) -> list[Item]:
        # Returns all items in inventory
        return self.inventory


    def getAvailableStorageUnits(self) -> list[str]:
        # Returns names of allowed storage units
        return self.availableStorageUnits


    def addAvailableStorage(self, unitName: str):
        # Adds a storage unit name to allowed list
        self.availableStorageUnits.append(unitName)
   
    def updateAvailableItems(self):
        for unit in self.getStorageUnits():
            for value in unit.getItemCategories():
                if not self.availableItems.__contains__(value):
                    self.availableItems.append(value)


    def updateMaxCapacity(self):
        # Updates capacity based on all storage units
        self.capacity = self.getTotalCapacity()
        self.updateAvailableItems()


    def addStorageUnit(self, unit=StorageUnit) -> bool:
        # Adds a storage unit if allowed, updates capacity
        unitName = unit.getName()
        if self.getAvailableStorageUnits().__contains__(unitName):
            for i in range(len(self.getStorageUnits())):
                if self.storage[i].getName() == unitName:
                    self.storage[i].addCount(unit.getCount())
                    self.updateMaxCapacity()
                    return True
            self.storage.append(unit)
            self.updateMaxCapacity()
            return True
        self.updateMaxCapacity()
        return False


    def removeStorageUnit(self, name: str, count: int):
        # Removes 'count' from a storage unit, deletes if count <= 0
        for i in range(len(self.getStorageUnits())):
            if self.storage[i].getName() == name:
                self.storage[i].addCount(count * -1)
                if self.storage[i].getCount() <= 0:
                    self.storage.remove(self.storage[i])
                break


    def getTotalCapacity(self, optionalCategory:str='') -> int:
        # Sums max items for all storage units, optionally by category
        units = self.getStorageUnits()
        count = 0
        for unit in units:
            if (optionalCategory == '') or (unit.canHoldCategory(optionalCategory)):
                count += unit.getCapacity()
        return count


    def getTotalEnergyUsage(self) -> int:
        # Sums power rating for all storage units
        sum = 0
        for unit in self.getStorageUnits():
            sum += unit.getPowerRating()
        return sum


    def __str__(self):
        # Returns a string summary of inventory and storage units
        stock = self.getTotalStock()
        capacity = self.getCapacity()
        canHoldStr = ", ".join(self.getAvailableItems())
        val = f"Capacity: {stock}/{capacity}, Can hold: [{canHoldStr}], Items: ["
        i = 0
        for item in self.listItems():
            val = val + str(item)
            i += 1
            if i != len(self.listItems()):
                val += ", "
        val = val + "]\nStorage Units: ["
        for item in self.getStorageUnits():
            val += f"{item.getName()} x{item.getCount()}, "
        val += "]"
        return val

def _testing():
    inv = Inventory()
    shelf = StorageUnit("shelf")


    inv.addAvailableStorage('shelf')
    inv.addStorageUnit(shelf)


    inv.addStock('Apple', 5)
    print(inv)
    print()


    #inv.addAvailableItem('Apple')
    inv.addStock('Apple', 5)
    print(inv)
    print()


    inv.addStock('Apple', 15)
    print(inv)
    print()


    freezer = StorageUnit('freezer')
    inv.addAvailableStorage('freezer')
    inv.addStorageUnit(freezer)
    print(inv)


    inv.addStorageUnit(StorageUnit('freezer'))
    print(inv)

if __name__ == "__main__":
    _testing()


# storage = ItemStorage(10)
# print(storage)
# storage.addCapacity(20)
# print(storage)
# storage.addAvailableItem("Apple")
# storage.addStock("Apple", 5)
# print(storage)
# storage.removeItem("Apple", 2)
# print(storage)


# storage.addStock("Carrot", 3)
# print(storage)
# storage.addAvailableItem("Carrot")
# storage.addStock("Carrot", 3)
# print(storage)


# storage.removeItem("Apple", 3)
# print(storage)


# storage.removeItem("Carrot", 2)
# print(storage)
# storage.removeItem("Carrot", 1)
# print(storage)



