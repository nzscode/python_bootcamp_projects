from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
user_choice = screen.textinput("winning_color", "Who will win the race? "
                                                "\nviolet, blue, green, yellow, orange or red ").lower()


race_border = Turtle()
race_border.hideturtle()
violet = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
red = Turtle()

violet.shape("turtle")
blue.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
orange.shape("turtle")
red.shape("turtle")

race_end_xcor = 200

race_border.hideturtle()
race_border.penup()
race_border.pensize(2)
race_border.setposition(-95, 10)
race_border.pendown()
race_border.forward(95 + race_end_xcor)
race_border.setheading(270)
race_border.forward(170)
race_border.setheading(180)
race_border.forward(95 + race_end_xcor)
race_border.setheading(90)
race_border.forward(170)

violet.shape("turtle")
blue.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
orange.shape("turtle")
red.shape("turtle")

violet.color("violet")
blue.color("blue")
green.color("green")
yellow.color("yellow")
orange.color("orange")
red.color("red")
violet.pensize(8)
blue.pensize(8)
green.pensize(8)
yellow.pensize(8)
orange.pensize(8)
red.pensize(8)
violet.penup()
blue.penup()
green.penup()
yellow.penup()
orange.penup()
red.penup()

violet.setposition(-100, 0)
blue.setposition(-100, -30)
green.setposition(-100, -60)
yellow.setposition(-100, -90)
orange.setposition(-100, -120)
red.setposition(-100, -150)

winner = ""
continue_race = True
while continue_race:
    violet_movement = random.randint(1, 10)
    violet.forward(violet_movement)

    blue_movement = random.randint(1, 10)
    blue.forward(blue_movement)

    green_movement = random.randint(1, 10)
    green.forward(green_movement)

    yellow_movement = random.randint(1, 10)
    yellow.forward(yellow_movement)

    orange_movement = random.randint(1, 10)
    orange.forward(orange_movement)

    red_movement = random.randint(1, 10)
    red.forward(red_movement)

    violet_position = round(violet.xcor())
    blue_position = round(blue.xcor())
    green_position = round(green.xcor())
    yellow_position = round(yellow.xcor())
    orange_position = round(orange.xcor())
    red_position = round(red.xcor())

    if violet_position >= race_end_xcor:
        continue_race = False
        winner = "violet"
        print("Violet won!")
        break
    elif blue_position >= race_end_xcor:
        continue_race = False
        winner = "blue"
        print("Blue won!")
        break
    elif green_position >= race_end_xcor:
        continue_race = False
        winner = "green"
        print("Green won!")
        break
    elif yellow_position >= race_end_xcor:
        continue_race = False
        winner = "yellow"
        print("Yellow won!")
        break
    elif orange_position >= race_end_xcor:
        continue_race = False
        winner = "orange"
        print("Orange won!")
        break
    elif red_position >= race_end_xcor:
        continue_race = False
        winner = "red"
        print("Red won!")
        break

if winner == user_choice:
    print("Good choice.")
else:
    print(f"Bad choice, {user_choice} did not win.")

screen.exitonclick()
