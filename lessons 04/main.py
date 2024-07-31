from choice import  Choice
from category import Category
from menu import Menu
from logger import logger

if __name__ == '__main__':
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

