import random
import hand_movements

user_choice = int(input('Choose 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
comp_choice = random.randint(0, 2)
if user_choice == 0:
    print(f'Your choice: \n{hand_movements.rock}')
elif user_choice == 1:
    print(f'Your choice: \n{hand_movements.paper}')
else:
    print(f'Your choice: \n{hand_movements.scissors}')

if comp_choice == 0:
    print(f'Computer choice: \n{hand_movements.rock}')
elif comp_choice == 1:
    print(f'Computer choice: \n{hand_movements.paper}')
else:
    print(f'Computer choice: \n{hand_movements.scissors}')

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