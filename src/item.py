class Item:
    def __init__(self, itemName, iDescription):
        self.itemName = itemName
        self.iDescription = iDescription

    def onGet(self, itemName):
        print(f"{self.itemName} has been added to your inventory.")

    def onDrop(self, itemName):
        print(f"You have dropped {self.itemName}.")

    def __str__(self):
        return f"{self.itemName}, {self.iDescription}"