from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

torch = Item('torch', "A flickering light in a place surrounded in darkness.")
key = Item('key', "An old rusted key. This might be useful later. Probably not.")

room['outside'].items.append(torch)
room['overlook'].items.append(key)


def try_direction(direction, current_room):
    attribute = direction + '_to'

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    elif direction == 'm' or direction == 'i':
        return current_room
    else:
        print(">>You can't go that way<<\n")
        return current_room

    # Make a new player object that is currently in the 'outside' room.
player = Player(room["outside"])
print("\n")
# print(room["outside"].items)
    # Write a loop that:
    #
    # * Prints the current room name
while True:
    print('Welcome to your new adventure. Press N, E, S, W to move. \n    Press i to see your inventory. \n    Press m to see all items in the room. \n    Good luck! \n\n')
    print(f"Your are currently here: \n    {player.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"    {textwrap.fill(player.current_room.description)}")
    # print(player.current_room.itemsInRoom(), "items in current room")
    # print(player.items, "items in inventory")
    # * Waits for user input and decides what to do.
    s = input("\n>").lower().split()
    
    if len(s) == 1:

        s = s[0][0]

        if s == 'q':
            break

        if s == 'i':
            print(f"\nThe items in your inventory are: {player.items}\n")

        if s == 'm':
            print(f"\nThe items in the current room are: {player.current_room.itemsInRoom()}\n")
            
        player.current_room = try_direction(s, player.current_room)

    elif len(s) == 2:
        first_word = s[0]
        second_word = s[1]

        def try_getItem(item, current_room):

            if [second_word] in [current_room.items]:
                print(f'\nYou have added the {second_word} to your inventory!\n')
                current_room.removeItem(second_word)
                player.addItem(second_word)
                return current_room
            else:
                print('\nitem not here\n')
                return current_room

        def try_dropItem(item, current_room):
            
            if [second_word] in [player.items]:
                print('\nYou have dropped the item from your inventory. Come back later to pick it up.')
                current_room.addItem(Item(second_word, 'You dropped this earlier.\n'))
                player.removeItem(second_word)
                return current_room
            else:
                print('\nitem not in inventory\n')
                return current_room

        if first_word in ['get', 'drop']:
            if first_word == 'get':
                player.current_room = try_getItem(second_word, player.current_room)
                # print(f'get {second_word}')
            elif first_word == 'drop':
                player.current_room = try_dropItem(second_word, player.current_room)
                # print(f'drop {second_word}')
        else:
            print('Use get or drop')
    else:
        print("I don't understand that")
        continue
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
