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

    def __str__(self):
        cart_contents = '\n'.join(f"{product.name} (things:{quantity}) - prise:{product.price * quantity:.2f}"
        for product, quantity in self.items)
        return f"Cart:\n{cart_contents}\nTotal amount: {self.suma():.2f}"


product1 = Product("water", 6.00)
product2 = Product("milk", 2.99,)
product3 = Product("banana", 4.99,)
product4 = Product("ice coffe", 8.00,)
product5 = Product("bread", 1,)

cart = Cart()
cart.add_product(product1, 4)
cart.add_product(product2, 4)
cart.add_product(product3, 4)
cart.add_product(product4, 4)
cart.add_product(product5, 4)
print(cart)

# Task 2
class Errorr(Exception):
    def __init__(self, discount_percentage, message="This card"):
        self.discount_percentage = discount_percentage
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"An error has occurred: {self.message} with discount {self.discount_percentage}%"
class Discount:
    def discount(self):
        return 0

class RegularDiscount(Discount):
    def discount(self):
        return 0.1

class ChristmasDiscount(Discount):
    def discount(self):
        return 0.2

class SilverDiscount(Discount):
    def discount(self):
        return 100

class Order:
    def __init__(self, cart: Cart, discount: Discount):
        self.cart = cart
        self.discount = discount

    def total(self):
        discount_value = self.discount.discount()
        if discount_value > 1:
            raise Errorr(discount_value)

if __name__ == '__main__':

    type_discount = input("Enter discount type: ")
    if type_discount == "regular":
        discount = RegularDiscount()
    elif type_discount == "christmas":
        discount = ChristmasDiscount()
    elif type_discount == "silver":
        discount = SilverDiscount()
    else:
        discount = Discount()

    order = Order(cart, discount)
    print(order.total())