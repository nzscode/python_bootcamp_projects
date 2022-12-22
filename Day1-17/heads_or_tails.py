import random


class HeadsOrTails:
    choice = random.randint(0, 1)
    if choice == 0:
        print("Heads")
    else:
        print("Tails")