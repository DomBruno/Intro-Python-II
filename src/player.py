# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

        def __str__(self):
            return f'{self.name}\'s location: {self.current_room}'

        def move(self, direction): 
            if getattr(self.current_room, f"{direction}") is not None: 
                self.current_room = getattr(self.current_room, f"{direction}") 
            else: print("------- sorry, you cannot move in that direction") 