from room import Rooms
from item import Item
from player import Player

# Declare all the rooms

item = {
    'lantern':  Item("Lantern", True),
    'rusty key':  Item("Rusty Key", False),
    'pen':  Item("Pen", False),
    'torch':  Item("Torch", True),
    'silver coin':  Item("Silver Coin", False)
}

room = {
    'outside':  Rooms("Outside Cave Entrance", "North of you, the cave mount beckons", [item["lantern"].name], False),

    'foyer':    Rooms("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [item["rusty key"].name], False),

    'overlook': Rooms("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [item["pen"].name], True),

    'narrow':   Rooms("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [item["torch"].name], False),

    'treasure': Rooms("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [item["silver coin"].name], False),
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

# print(room['treasure'].s_to)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("B", "outside")

# print(player.room)
# print(item[room['outside'].items[0].lower()].lightsource)
# print(player.inventory)
# print(room[player.room].is_lit)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

active = True
has_light = False
while active:

    if player.room == 'outside':

        def check_for_light():
            if room[player.room].is_lit == True:
                global has_light
                has_light = True
            elif room[player.room].is_lit == False:
                has_light = False
                for i in player.inventory:
                    if item[i.lower()].lightsource == True:
                        has_light = True

        check_for_light()

        print("")
        print("Current inventory: ", player.inventory)

        if has_light == True:
            print(room[player.room])
            print(room[player.room].items)
        else:
            print("Its pitch black!")
            print(room[player.room].items)
        print("")

        direction = input('You can only head North from here. Press N to head North, P to pickup items, or Q to quit').lower()
        if direction[0] == 'n':
            player.room = 'foyer'
        elif direction[0] == 'q':
            active = False
        elif direction[0] == 'p':
            player.inventory = player.inventory + room['outside'].items
            room['outside'].items = []
        elif direction[0] == 'd':
            room['outside'].items = room['outside'].items + player.inventory
            player.inventory = []
        else:
            direction = input('Please choose a valid option. You can only head North from here. Press N to head North, P to pickup items, or Q to quit').lower()

    if player.room == 'foyer':
        def check_for_light():
            if room[player.room].is_lit == True:
                global has_light
                has_light = True
            elif room[player.room].is_lit == False:
                has_light = False
                for i in player.inventory:
                    if item[i.lower()].lightsource == True:
                        has_light = True

        check_for_light()
        print("")
        print("Current inventory: ", player.inventory)
        if has_light == True:
            print(room[player.room])
        else:
            print("Its pitch black!")
        print("")
        direction = input('In which direction will you proceed? N, E, or S? Press P to pickup items').lower()
        if direction[0] == 'n':
            player.room = 'overlook'
        elif direction[0] == 'e':
            player.room = 'narrow'
        elif direction[0] == 's':
            player.room = 'outside'
        elif direction[0] == 'p':
            player.inventory += room['foyer'].items
            room['foyer'].items = []
        elif direction[0] == 'd':
            room['outside'].items = room['outside'].items + player.inventory
            player.inventory = []
        elif direction[0] == 'q':
            active = False
        else:
            direction = input('Please choose another direction: N, E, or S? ')

    if player.room == 'overlook':
        def check_for_light():
            if room[player.room].is_lit == True:
                global has_light
                has_light = True
            elif room[player.room].is_lit == False:
                has_light = False
                for i in player.inventory:
                    if item[i.lower()].lightsource == True:
                        has_light = True

        check_for_light()
        print("")
        print("Current inventory: ", player.inventory)
        if has_light == True:
            print(room[player.room])
        else:
            print("Its pitch black!")
        print("")
        direction = input('In which direction will you proceed? S? Press P to pickup items').lower()
        if direction[0] == 's':
            player.room = 'foyer'
        elif direction[0] == 'p':
            player.inventory += room['overlook'].items
            room['overlook'].items = []
        elif direction[0] == 'd':
            room['outside'].items = room['outside'].items + player.inventory
            player.inventory = []
        elif direction[0] == 'q':
            active = False
        else:
            direction = input('Please choose another direction: S? ')

    if player.room == 'narrow':
        def check_for_light():
            if room[player.room].is_lit == True:
                global has_light
                has_light = True
            elif room[player.room].is_lit == False:
                has_light = False
                for i in player.inventory:
                    if item[i.lower()].lightsource == True:
                        has_light = True

        check_for_light()
        print("")
        print("Current inventory: ", player.inventory)
        if has_light == True:
            print(room[player.room])
        else:
            print("Its pitch black!")
        print("")
        direction = input('In which direction will you proceed? N, or W? Press P to pickup items').lower()
        if direction[0] == 'n':
            player.room = 'treasure'
        elif direction[0] == 'w':
            player.room = 'foyer'
        elif direction[0] == 'p':
            player.inventory += room['narrow'].items
            room['narrow'].items = []
        elif direction[0] == 'd':
            room['outside'].items = room['outside'].items + player.inventory
            player.inventory = []
        elif direction[0] == 'q':
            active = False
        else:
            direction = input('Please choose another direction: N, or W? Press P to pickup items')

    if player.room == 'treasure':
        def check_for_light():
            if room[player.room].is_lit == True:
                global has_light
                has_light = True
            elif room[player.room].is_lit == False:
                has_light = False
                for i in player.inventory:
                    if item[i.lower()].lightsource == True:
                        has_light = True

        check_for_light()
        print("")
        print("Current inventory: ", player.inventory)
        if has_light == True:
            print(room[player.room])
        else:
            print("Its pitch black!")
        print("")
        direction = input('In which direction will you proceed? S? Press P to pickup items').lower()
        if direction[0] == 's':
            player.room = 'narrow'
        elif direction[0] == 'p':
            player.inventory += room['treasure'].items
            room['treasure'].items = []
        elif direction[0] == 'd':
            room['outside'].items = room['outside'].items + player.inventory
            player.inventory = []
        elif direction[0] == 'q':
            active = False
        else:
            direction = input('Please choose another direction: S? ')