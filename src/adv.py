from room import Room
from player import Player
from item import Item
import sys
# Declare all the rooms

item = {
    'boomstick': Item("Boomstick", "A trusty Boomstick", 75),
    'book': Item("Necronomicon", "A horrid book bound in human skin", 300),
    }

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item["boomstick"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item["book"]),

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

# Make a new player object that is currently in the 'outside' room.
player = Player('Raistlin', room['outside'], [None])
game_start = True

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

def user_command():
    global game_start
    if game_start:
        game_start = False
        input('Welcome to Miniscule Cave Adventure!\n\nHit enter to continue\n\n\n')
    else:
        direction = input('[n]orth [s]outh [e]ast [w]est [i]nventory [q]uit \nYou may also [t]ake or [d]rop items.\n\n')
        return direction

player_move = user_command()

#Command Parser
while player_move != "q":
    print(player.current_room)
    print(player.current_room.desc)
    print(f'{player.current_room.items}')
    print('\n')
    player_move = user_command()

    if player_move == 'i':
        # Displays player inventory
        player.inv() 
    elif player_move != 'q':
        # Displays current room name and desc, appends user directional input to '_to' 
        player.move(f'{player_move}_to')
        # Exits program and Says Goodbye
    else:
        sys.exit('Thank you for playing Miniscule Cave!')