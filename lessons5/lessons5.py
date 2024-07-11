from math import gcd
# Task 1
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


    def add_product(self, product, quantity,):

        self.items.append((product, quantity))

    def suma(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.items.extend(other.items)
        else:
            raise('You cannot have more than 1 cart')
        return self

    def __str__(self):
        cart_contents = '\n'.join(f"{product.name} (things:{quantity}) - prise:{product.price * quantity:.2f}"
        for product, quantity in self.items)
        return f"Cart:\n{cart_contents}\nTotal amount: {self.suma():.2f}"


product1 = Product("water", 6.00)
product2 = Product("milk", 2.99,)
product3 = Product("banana", 4.99,)
product4 = Product("ice coffe", 8.00,)
product5 = Product("bread", 1,)

cart_one = Cart()
cart_one.add_product(product1, 4)
cart_one.add_product(product2, 4)
cart_one.add_product(product3, 4)
cart_one.add_product(product4, 4)
cart_one.add_product(product5, 4)


product6 = Product("apple", 6.00)
product7 = Product("butter", 2.99,)
product8 = Product("nivea man", 4.99,)
product9 = Product("kokos", 8.00,)
product10 = Product("pan", 1,)

cart_two = Cart()
cart_two.add_product(product6, 4)
cart_two.add_product(product7, 4)
cart_two.add_product(product8, 4)
cart_two.add_product(product9, 4)
cart_two.add_product(product10, 4)
cart_one += cart_two
print(cart_one)

# Task 3
class ProperFraction:

    def __init__(self, x, y):
        if x == 0:
            raise ValueError('X cannot be zero(0)')
        if x == 0:
            raise ValueError('X cannot be zero(0)')
        self.x = x
        self.y = y
        self.comparison()

    def comparison(self):
        com = gcd(self.x, self.y)
        self.x //= com
        self.y //= com




    def __add__(self, other):
        return self.x + other.y

    def __eq__(self, other):
        return self.x == other.y

    def __sub__(self, other):
        return self.x - other.y

    def __mul__(self, other):
        return self.x * other.y

    def __lt__(self, other):
        return self.x < other.y

    def __le__(self, other):
        return self.x <= other.y

    def __gt__(self, other):
        return self.x > other.y

    def __ge__(self, other):
        return self.x >= other.y


x1 = ProperFraction(9, 7)
y1 = ProperFraction(10, 9)


print(f'x1 + y1 = {x1 + y1}')
print(f'x1 - y1 = {x1 - y1}')
print(f'x1 * y1 = {x1 * y1}')
print(f'x1 < y1')
print(f'x1 <= y1')
print(f'x1 > y1')
print(f'x1 >= y1')
print(f'x1 == y1')
