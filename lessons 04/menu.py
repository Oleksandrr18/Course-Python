from category import Category
class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_category = '\n'.join(str(category) for category in self.categories)

        return f"Menu:\n{menu_category}"


