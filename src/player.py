# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.current_room}"

    def addItem(self, item):
        self.items.append(item)
    
    def removeItem(self, item):
        self.items.remove(item)

        