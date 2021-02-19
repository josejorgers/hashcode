

class Pizza:

    def __init__(self, id, ingredients):
        self.id = id
        self.ingredients = ingredients

    def __str__(self):

        return f'PIZZA - {self.id}: {self.ingredients}'