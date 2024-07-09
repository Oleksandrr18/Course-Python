from logger import logger
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


