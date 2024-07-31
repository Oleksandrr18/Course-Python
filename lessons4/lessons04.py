import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler('data.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Task 2
class Choice:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        if int(price) < 1:
            logger.error('An error occurred, length is 0')
            raise ValueError('An error occurred, length is 0')
        logger.info(f'{name}: {description} = {price}')

    def __str__(self):
        return f'{self.name} - {self.description}: ${self.price:.2f}'


class Category:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        c_category = '\n  '.join(str(dish) for dish in self.dishes)
        return f"{self.name}:\n  {c_category}"


class Menu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_category = '\n'.join(str(category) for category in self.categories)

        return f"Menu:\n{menu_category}"


dish1 = Choice('Beef steak', 'beef, fries, salad', 40)
dish2 = Choice('Shrimp tempura', 'shrimp', 6)
dish3 = Choice('Burger', 'pork cutlet, onion, tomato, signature sauce', 35)
dish4 = Choice('Parmigiano salad', 'eggplant, tomato, lettuce, mozzarella cheese', 16)
dish5 = Choice('Strawberry flambé with ice cream', 'strawberries, brandy/cognac, ice cream', 10)

main_dishes = Category("Main dishes")
snacks = Category("Snacks")
desserts = Category("Desserts")

main_dishes.add_dish(dish1)
main_dishes.add_dish(dish2)
main_dishes.add_dish(dish3)
snacks.add_dish(dish4)
desserts.add_dish(dish5)

menu = Menu()
logger.info('Menu created')
menu.add_category(main_dishes)
menu.add_category(snacks)
menu.add_category(desserts)

print(menu)