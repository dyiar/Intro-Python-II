# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items

    def itemsInRoom(self):
        if len(self.items) == 0:
            return "No Items"
        else:
            roomItems = []
            for item in self.items:
                roomItems.append(item.itemName)
            self.items = roomItems
            return roomItems

    def listItems(self):
        if len(self.items) == 0:
            print('No items')
        else:
            for item in self.items:
                print(f"{item.itemName}: {item.iDescription}")

    def removeItem(self, item):
        self.items.remove(item)

    # def addItem(self, item):
    #     self.items.append(item)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.items}"