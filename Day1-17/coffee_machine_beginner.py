MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
coffee_machine_off = False


# TODO: 1. Turn machine off when option is selected.
def turn_off():
    """Turns off machine."""
    global coffee_machine_off
    coffee_machine_off = True


# TODO: 13. Update the resources by subtracting the respective ingredients of the made coffee
#  from the resources total. Also update the money. Must use a global declaration for the money variable,
#  so it can be changed from inside the function.
def update_resources_money(user_choice, cost):
    """Updates resources and money after every order."""
    global money
    new_water = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["water"] = new_water
    new_milk = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
    resources["milk"] = new_milk
    new_coffee = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    resources["coffee"] = new_coffee
    money += cost


# TODO: 2. Print out a report of available resources.
def report():
    """prints out a report of remaining resources and money in the machine."""
    print(f'Water: {resources["water"]}ml')
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


# TODO: 9. Ask user for coins and calculate total. Make sure to convert all to float.
def insert_coins():
    """Asks and calculates total from the coins inserted."""
    print("Please insert coins: ")
    quarters = float(int(input("How many quarters? ")) * 0.25)
    dimes = float(int(input("How many dimes? ")) * 0.10)
    nickels = float(int(input("How many nickels? ")) * 0.05)
    pennies = float(int(input("How many pennies? ")) * 0.01)
    total = quarters + dimes + nickels + pennies
    return total


    # TODO: 10. If total is less that the cost of the coffee chosen from MENU,
    #  then respond with a sorry and refund the money.
def enough_money(total_money, coffee_choice):
    """Checks if the money inserted is enough for the specific price of the chosen coffee."""
    if total_money < MENU[coffee_choice]["cost"]:
        print("Sorry, that's not enough money. Money refunded")
        # TODO: 11. if the coffee cost is less than the total value of coins inserted, then return the change.
    else:
        change = total_money - MENU[coffee_choice]["cost"]
        print(f"Here is your change: ${change:.2f}")
        print(f"Here is your {coffee_choice}. Enjoy!")
        # TODO: 12. Update the resources and money by calling update_resources_money()
        update_resources_money(coffee_choice, MENU[coffee_choice]["cost"])


def is_resource_enough(coffee_choice):
    """Checks if there are enough remaining resources to make the chosen coffee."""
    for ingredient in MENU[coffee_choice]["ingredients"]:
        if resources[ingredient] <= MENU[coffee_choice]["ingredients"][ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return False
    return True


# TODO: 3. Ask user what they want.
def choice():
    user_choice = input("What would you like?  (Espresso / Latte / Cappuccino):  ").lower()
    # TODO: 4. If user chooses off, call turn_off() from TODO: 1.
    if user_choice == "off":
        turn_off()
        return
    # TODO: 5. If user chooses report, call report() from TODO: 2.
    elif user_choice == "report":
        report()
        # TODO: 6. If user chooses an item that can be found in the MENU, then show user the price.
    elif user_choice in MENU:
        print(f"The price of a {user_choice} is: ${MENU[user_choice]['cost']:.2f}")
        # TODO: 7. Check resources quantities against menu ingredients quantities,
        #  and return a sorry message if not enough using is_enough() .
        if is_resource_enough(user_choice):
            # TODO: 8. If there are enough resource quantities, then ask user for coins using TODO: 9.
            total = insert_coins()
            enough_money(total, user_choice)
        else:
            return
            # TODO: 14. Call on the choice function again to make another coffee or until coffee_machine_off is
    #  triggered because the off() function was triggered or because the flag was triggered
    #  at the lack of available resources.
    choice()


choice()
