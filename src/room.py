# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, n_to = None, s_to= None, e_to= None, w_to = None, items = []):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        item_list = ""
        for item in self.items:
            item_list += item.item_name + "\n"
        # item_list = [f'{item.name}\n' for item in self.items]
        return f"You see a\n{item_list}"