import random


class Roulette:
    def __init__(self):
        print("Welcome to banker roulette")

    def PickAName(self):
        names_input = input("Please enter names separated by a comma and space.")
        names = names_input.split(", ")
        r_num = random.randint(0, len(names)-1)
        print(names[r_num])