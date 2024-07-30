from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parameter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius
    def parameter(self):
        return 2 * math.pi * self.radius

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width + self.height

    def parameter(self):
        return 2 * (self.width + self.height)

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def parameter(self):
        return self.a + self.b + self.c


circle = Circle(4)
rectangle = Rectangle(6, 9)
triangle = Triangle(3, 8, 5)

print(f'Circle area:{circle.area()}, Parameter:{circle.parameter()}')
print(f'Rectangle area:{rectangle.area()}, Parameter:{rectangle.parameter()}')
print(f'Triangle area:{triangle.area()}, Parameter:{triangle.parameter()}')

# Task 2
from abc import ABC, abstractmethod

class Payment_Methods(ABC):
    @abstractmethod
    def make_a_payment(self, summa):
        pass

class Credit_card(Payment_Methods):
    def __init__(self, card_number, other, validity_of_the_term, ccv):
        self.card_number = card_number
        self.other = other
        self.validity_of_the_term = validity_of_the_term
        self.ccv = ccv

    def make_a_payment(self, summa):
        print(f'A transfer was made for the amount: {summa} UA, on the card: {self.card_number}')


class Bank_transfer(Payment_Methods):
    def __init__(self, card_number, recipient, bank):
        self.card_number = card_number
        self.recipient = recipient
        self.bank = bank
    def make_a_payment(self, summa):
        print(f'A transfer was made for the amount: {summa} '
              f'UA, on the card: {self.card_number}, through the bank: {self.bank}')


class Online_wallet(Payment_Methods):
    def __init__(self, id_number,  provider):
        self.id_number = id_number
        self.provider = provider
    def make_a_payment(self, summa):
        print(f'A transfer was made for the amount: {summa} '
              f'UA, to id number: {self.id_number}, provider: {self.provider}')

class Payment_Processor:
    def __init__(self):
        self.available_funds = []

    def adding_payment(self,means_of_payment):
        self.available_funds.append(means_of_payment)

    def execution_of_payment(self,index, summa):
        try:
            means_of_payment = self.available_funds[index]
            means_of_payment.make_a_payment(summa)
        except IndexError:
            raise ValueError(f'Index {index} is out of range')

payment_processor = Payment_Processor()
payment_processor.adding_payment(Credit_card('123 333 563 7878', 'Alex', '12/26', '895'))
payment_processor.adding_payment(Bank_transfer('123 333 563 7878', 'Alex', 'Privat24'))
payment_processor.adding_payment(Online_wallet('123 333 563 7878', 'PayPay'))

payment_processor.execution_of_payment(0, 100)
payment_processor.execution_of_payment(1, 100)
payment_processor.execution_of_payment(2, 100)







