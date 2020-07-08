# Implement a class to hold room information. This should have name and
# description attributes.
class Rooms:
    def __init__(self, name, description, items, is_lit, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.is_lit = is_lit
        self.items = items

    def __str__(self):
        return f'Current location: {self.name}. Description: {self.description} Items in room: {self.items}'