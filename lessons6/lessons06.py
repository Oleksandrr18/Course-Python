# Task 1
class Iterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            product, quantity = item
            return f'{product}: {quantity}'
        raise StopIteration


class Error(Exception):
    def __init__(self, product_name, message):
        self.product_name = product_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"An error has occurred this product:({self.message}) costs zero(0) please select another."


class Product(Error):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        if price == 0:
            raise Error(self, name)

    def __str__(self):
        return f'{self.name} {self.price}.'


class Cart(Error):
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity, ):

        self.items.append((product, quantity))

    def suma(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.items.extend(other.items)
        else:
            raise ('You cannot have more than 1 cart')
        return self

    def __str__(self):
        cart_contents = '\n'.join(f"{product.name} (things:{quantity}) - prise:{product.price * quantity:.2f}"
                                  for product, quantity in self.items)
        return f"Cart:\n{cart_contents}\nTotal amount: {self.suma():.2f}"

    def __iter__(self):
        return Iterator(self.items)


product1 = Product("water", 6.00)
product2 = Product("milk", 2.99, )
product3 = Product("banana", 4.99, )
product4 = Product("ice coffe", 8.00, )
product5 = Product("bread", 1, )

cart_one = Cart()
cart_one.add_product(product1, 4)
cart_one.add_product(product2, 4)
cart_one.add_product(product3, 4)
cart_one.add_product(product4, 4)
cart_one.add_product(product5, 4)

product6 = Product("apple", 6.00)
product7 = Product("butter", 2.99, )
product8 = Product("nivea man", 4.99, )
product9 = Product("kokos", 8.00, )
product10 = Product("pan", 1, )

cart_two = Cart()
cart_two.add_product(product6, 4)
cart_two.add_product(product7, 4)
cart_two.add_product(product8, 4)
cart_two.add_product(product9, 4)
cart_two.add_product(product10, 4)
cart_one += cart_two

for item in cart_one:
    print(item)

# Task 2
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

class Iterator:
    def __init__(self, categories):
        self.categories = categories
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.categories):
            category = self.categories[self.index]
            self.index += 1
            return category
        raise StopIteration
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

    def __iter__(self):
        return Iterator(self.categories)

    def __getitem__(self, item):
        return self.categories[item]

    def __len__(self):
        return len(self.categories)


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

for item in menu:
    print(item)


