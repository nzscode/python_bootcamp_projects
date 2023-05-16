import math
import random

print("Functions: Lesson 4.1")
def printLines():
    print("I will not copy and paste code.")
    print("I will use Camel Case when writing class names.")
    print("I will use lower case and separate words with underscores when writing function names.")
    print("I will use lower case and separate words with underscores when writing variables names.")

for i in range(5):
    printLines()
    print("\n")

print("Functions: Lesson 4.2")
def tip_the_waiter(bill):
    '''
    :param bill: a float value
    :return: multiplies bill by 0.15 for 15% tax.
    '''

    tip = bill*0.15
    print(f"You service was wonderful! Please accept this tip: ${tip}")

tip_the_waiter(53.50)

print("Functions: Lesson 4.5")
def areaSquare(side):
    '''
    :param side: an integer
    :return: returns the square of the side
    '''
    if side < 0:
        return "Impossible"
    else:
        return side*side

side = 5
area = areaSquare(side)

print(f"The area of a square with the side :{side} is {area}")

print("Functions: Challenge 1")
response = input("Let's play Rock Paper Scissors."
                 "\nWhen I say 'shoot', Choose: rock, paper, or scissors."
                 "\nAre you ready? Write 'yes' if you are\n").lower()
if response == "yes":
    user_choice = input("Great!\nrock - paper - scissors, shoot!\nMake your choice and type it in:\n").lower()

    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("Draw")
    elif (user_choice == "rock" and comp_choice == "scissors") or (user_choice == "scissors" and comp_choice == "paper") or (user_choice == "paper" and comp_choice == "rock"):
        print("You win!")
    else:
        print("You lose.")
else:
    print("Darn, some other time.")
