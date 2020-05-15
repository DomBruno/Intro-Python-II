# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory: []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name}\'s location: {self.current_room}'

    def move(self, direction): 
        if getattr(self.current_room, f'{direction}') is not None: 
            self.current_room = getattr(self.current_room, f'{direction}') 
        else: print('------- sorry, you cannot move in that direction.')
        
    def take(self, item):
        for item in self.current_room.items:
            print(item)
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)

    def drop(self, item):
        for item in self.inventory.items:
            print(item)
        if item in self.inventory.items:
            self.current_room.items.append(item)
            self.inventory.items.remove(item)

    def inv(self):
        if len(self.inventory) > -1:
            for item in enumerate(self.inventory):
                print(str(item.name))
        else:
            print('You are not holding anything.')