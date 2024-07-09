
class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        c_category = '\n  '.join(str(dish) for dish in self.dishes)
        return f"{self.name}:\n  {c_category}"