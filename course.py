class Discount:
    def discount(self, total_price):
        return total_price

class RegularDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.90

class SilverDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.60

class GoldDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.30

class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total(self, order_amount):
        discounted_price = self.discount.discount(order_amount)
        return discounted_price

def place_order():
    name = input("Enter your name: ").lower()
    card_type = input("Enter your loyalty card type (Regular, Silver, Gold): ").lower()
    order_amount = float(input("Enter the total order amount: "))

    if card_type == "regular":
        discount = RegularDiscount()
    elif card_type == "silver":
        discount = SilverDiscount()
    elif card_type == "gold":
        discount = GoldDiscount()
    else:
        print("Invalid card type. No discount applied.")
        discount = Discount()

    client = Client(name, discount)
    final_price = client.get_total(order_amount)

    print(f"The final price after applying discount for {client.name} is: {final_price:.2f}")

place_order()
