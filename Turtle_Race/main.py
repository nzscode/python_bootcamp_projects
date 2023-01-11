from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
screen.setup(width = 500, height = 400)

race_distance = 100

print_text1 = Turtle()
print_text1.hideturtle()
print_text1.penup()
print_text1.setposition(-100, 125)
print_text2 = Turtle()
print_text2.hideturtle()
print_text2.penup()
print_text2.setposition(-100, 110)
race_border = Turtle()
race_border.hideturtle()
continue_race = False
user_input = screen.textinput("Make a choice:", "Pick a color: Red, Orange, Green, "
                                                "Hotpink, Blue, Indigo, or Violet? ").capitalize()
turtles = [
    {"turtle_name": "Tim",
     "turtle_color": "Red",
     },
    {"turtle_name": "Bob",
     "turtle_color": "Orange",
     },
    {"turtle_name":"Sha",
     "turtle_color": "Green",
     },
    {"turtle_name":"Rose",
     "turtle_color": "Hotpink",
     },
    {"turtle_name":"Nile",
     "turtle_color": "Blue",
     },
    {"turtle_name": "Zed",
     "turtle_color": "Indigo",
     },
    {"turtle_name":"Ann",
     "turtle_color": "Violet",
     }
]
colors = ["red", "orange", "green", "hotpink", "blue", "indigo", "violet"]
y_start_positions = [0, -30, 30, 60, -60, 90, -90]
all_turtles_list = []


def racing_field(distance):
    race_border.penup()
    race_border.pensize(2)
    race_border.setposition(-170, 100)
    race_border.pendown()
    race_border.forward(200 + distance)
    race_border.setheading(270)
    race_border.forward(170)
    race_border.setheading(180)
    race_border.forward(200 + distance)
    race_border.setheading(90)
    race_border.forward(170)
    race_border.setposition(110, 100)
    race_border.setheading(270)
    race_border.forward(170)


racing_field(race_distance)

# if user_input:
#     continue_race = True
continue_race =  True

for _ in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[_])
    turtle_name = turtles[_]
    turtle.penup()
    turtle.setposition(-150, y_start_positions[_])
    all_turtles_list.append(turtle)

while continue_race:
    for turtle in all_turtles_list:
        turtle_movement = random.randint(0, 10)
        turtle.forward(turtle_movement)
        if turtle.xcor() > race_distance:
            continue_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print_text1.write(f"You won, {winning_color.capitalize()} won!", font=("Lemon", 10, "bold"))
            else:
                print_text1.write(f"You lost, {winning_color.capitalize()} won!", font=("Lemon", 10, "bold"))