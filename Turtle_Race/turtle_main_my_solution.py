from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
screen.setup(width = 500, height = 400)

race_distance = 100
race_border = Turtle()
race_border.hideturtle()

bob = Turtle()
sha = Turtle()
lem = Turtle()
zob = Turtle()
ned = Turtle()
tim = Turtle()

bob.shape("turtle")
bob.penup()
sha.shape("turtle")
sha.penup()
lem.shape("turtle")
lem.penup()
zob.shape("turtle")
zob.penup()
ned.shape("turtle")
ned.penup()
tim.shape("turtle")
tim.penup()



def racing_field(race_distance):
    race_border.penup()
    race_border.pensize(2)
    race_border.setposition(-170, 70)
    race_border.pendown()
    race_border.forward(185 + race_distance)
    race_border.setheading(270)
    race_border.forward(170)
    race_border.setheading(180)
    race_border.forward(185 + race_distance)
    race_border.setheading(90)
    race_border.forward(170)
    race_border.setposition(175, 70)
    race_border.setheading(270)
    race_border.forward(170)


race_end_xcor = 200
racing_field(race_end_xcor)


def turtle_race():
    user_choice = screen.textinput("winning_color", "Who will win the race? "
                                                    "\nBob, Sha, Lem, Zob, Ned or Tim ").capitalize()
    print_text1 = Turtle()
    print_text1.hideturtle()
    print_text1.penup()
    print_text1.setposition(-100, 125)
    print_text2 = Turtle()
    print_text2.hideturtle()
    print_text2.penup()
    print_text2.setposition(-100, 110)



    tim.shape("turtle")
    bob.shape("turtle")
    sha.shape("turtle")
    lem.shape("turtle")
    zob.shape("turtle")
    ned.shape("turtle")

    bob.color("violet")
    sha.color("blue")
    lem.color("green")
    zob.color("hotpink")
    ned.color("orange")
    tim.color("red")
    bob.pensize(8)
    sha.pensize(8)
    lem.pensize(8)
    zob.pensize(8)
    ned.pensize(8)
    tim.pensize(8)

    print_text1.setposition(-170, 100)
    print_text2.setposition(-170, 75)
    bob.setposition(-165, 0)
    sha.setposition(-165, -30)
    lem.setposition(-165, -60)
    zob.setposition(-165, 30)
    ned.setposition(-165, 60)
    tim.setposition(-165, -90)

    winner = ""
    continue_race = True
    while continue_race:
        bob_movement = random.randint(1, 10)
        bob.forward(bob_movement)

        sha_movement = random.randint(1, 10)
        sha.forward(sha_movement)

        lem_movement = random.randint(1, 10)
        lem.forward(lem_movement)

        zob_movement = random.randint(1, 10)
        zob.forward(zob_movement)

        ned_movement = random.randint(1, 10)
        ned.forward(ned_movement)

        tim_movement = random.randint(1, 10)
        tim.forward(tim_movement)

        bob_position = round(bob.xcor())
        sha_position = round(sha.xcor())
        lem_position = round(lem.xcor())
        zob_position = round(zob.xcor())
        ned_position = round(ned.xcor())
        tim_position = round(tim.xcor())

        if bob_position >= race_end_xcor:
            winner = "Bob"
            print_text1.write("Bob won! (Violet)", font=("Lemon", 20, "bold"))
            continue_race = False
        elif sha_position >= race_end_xcor:
            winner = "Sha"
            print_text1.write("Sha won! (Blue)", font=("Lemon", 20, "bold"))
            continue_race = False
        elif lem_position >= race_end_xcor:
            winner = "Lem"
            print_text1.write("Lem won! (Green)", font=("Lemon", 20, "bold"))
            continue_race = False
        elif zob_position >= race_end_xcor:
            winner = "Zob"
            print_text1.write("Zob won! (Hot Pink)", font=("Lemon", 20, "bold"))
            continue_race = False
        elif ned_position >= race_end_xcor:
            winner = "Ned"
            print_text1.write("Ned won! (Orange)", font=("Lemon", 20, "bold"))
            continue_race = False
        elif tim_position >= race_end_xcor:
            winner = "Tim"
            print_text1.write("Tim won! (Red)", font=("Lemon", 20, "bold"))
            continue_race = False

    if winner == user_choice:
        print_text2.write("Good choice.", font=("Lemon", 20, "bold"))
    else:
        print_text2.write(f"Bad choice, {user_choice} did not win.", font=("Lemon", 20, "bold"))

    restart = screen.textinput("race restart", "restart race?\ny or n ").lower()
    if restart == 'y':
        turtle_race()
    else:
        screen.reset()


turtle_race()
screen.exitonclick()
