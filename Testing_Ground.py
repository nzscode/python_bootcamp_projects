Recipes = {}
recipe_name = input("what is the name of your recipe?\n").title()

add_ingredient = True


def enter_ingredients():
    ingredient = input("What is your ingredient?\n").lower()
    q_name = input("grams or cups\n").lower()
    quantity = input(f"How many {q_name} of {ingredient}?\n").lower()

while add_ingredient:
    a_ingredient = input("Add ingredient? Y or N\n").lower()
    if add_ingredient == "y":
        enter_ingredients()
    else:
        add_ingredient = False

enter_ingredients()
