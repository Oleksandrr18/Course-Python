class Discount:

    def discount(self, total_amount):
        return total_amount


class RegularDiscount(Discount):
    def discount(self, total_amount):
        return total_amount * 0.90


class SilverDiscount(Discount):
    def discount(self, total_amount):
        return total_amount * 0.60


class GoldDiscount(Discount):
    def discount(self, total_amount):
        return total_amount * 0.30



class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total(self, total_amount):
        discounted_price = self.discount.discount(total_amount)
        return discounted_price


def main():
    while True:
        name = input('Enter the name:').lower()
        duc = input('Enter the Regular:Silver:Gold:').lower()
        tot_amount = float(input('Enter the total amount:'))

        if duc == 'regular':
            discount = RegularDiscount()
        elif duc == 'silver':
            discount = SilverDiscount()
        elif duc == 'gold':
            discount = GoldDiscount()
        else:
            print('Invalid animal')
            continue
        client = Client(name, discount)
        final_price = client.get_total(tot_amount)
        print(f'Name: {client.name}, Total amount: {final_price}')

if __name__ == '__main__':
    main()