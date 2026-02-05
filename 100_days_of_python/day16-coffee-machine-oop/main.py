from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""STEP1 : PRINT REPORT"""
#creating the obj money_machine with the class MoneyMachine()
money_machine = MoneyMachine()
#creating the obj coffee_maker with the class CoffeeMaker()
coffee_maker = CoffeeMaker()
##creating the obj coffee_maker with the class CoffeeMaker() - step2.1
menu = Menu()

is_on = True

# access the report method in CoffeeMaker() and MoneyMaker() class
# coffee_maker.report()
# money_machine.report()

"""STEP2 : CHECK RESOURCES SUFFICIENT"""
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # we have to move that coffee_maker.report() method and money_machine.report()
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        # instead of printing drink going to tackle step2: resource sufficient
        # print(coffee_maker.is_resource_sufficient(drink)) - instead of print do proceed
        if coffee_maker.is_resource_sufficient(drink):
            # step 3 take payment from the user and process coins & check transac succesful
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        # short code :
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #     coffee_maker.make_coffee(drink)