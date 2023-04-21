import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('Choose 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_choice = random.randint(0, 2)
if user_choice == 0:
    print(f'Your choice: \n{rock}')
elif user_choice == 1:
    print(f'Your choice: \n{paper}')
else:
    print(f'Your choice: \n{scissors}')

if comp_choice == 0:
    print(f'Computer choice: \n{rock}')
elif comp_choice == 1:
    print(f'Computer choice: \n{paper}')
else:
    print(f'Computer choice: \n{scissors}')

if user_choice == 0 and comp_choice == 2:
    print("You won")
elif comp_choice == 0 and user_choice == 2:
    print("You lost")
elif user_choice == comp_choice:
    print("Draw")
elif user_choice > comp_choice:
    print("You won")
else:
    print("You lost")