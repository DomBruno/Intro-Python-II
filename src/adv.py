from room import Room
from player import Player
import sys
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

def get_travel_dir():
    global game_start
    if game_start:
        game_start = False
        input('Welcome to Miniscule Cave Adventure!\n\nHit enter to continue\n\n\n')
    else:
        direction = input('[n] North [s] South [e] East [w] West [q] Quit \n\n')
        return direction

player_move = get_travel_dir()


# Displays current room name and desc, appends user directional input to '_to' 
while player_move != "q":
    print(player.current_room)
    print(player.current_room.desc)
    print('\n')
    player_move = get_travel_dir()
    if player_move != 'q':
        player.move(f'{direction}_to')
    else:
        sys.exit('Thank you for playing Miniscule Cave!')