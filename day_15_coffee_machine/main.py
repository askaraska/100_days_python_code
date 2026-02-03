from pickle import GLOBAL
from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, false if ingredients are insufficient"""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"sorry, there is not enough {ingredient} in {order_ingredients[ingredient]}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert the coins")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.10
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources dictionary"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}'s coffee☕")

# TODO:1 Print the report of all coffee machine resources
is_on = True
while is_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == "off":
            is_on = False
        elif choice == "report":  #Print report.
            print(f"Water: {resources["water"]}ml")
            print(f"Milk:  {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money:${profit}")
        else:
        # drink = MENU[choice]
        # print(drink) instead of printing the drink,
        # im going to create function to compare order drink with resources
            drink =MENU[choice] # MENU[latte] =
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                #process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
