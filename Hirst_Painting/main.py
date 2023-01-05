# TODO 1: Import Colorgram Package:
# Go to FIle > Settings > Project Name > Python Interpreter >
# Type in Package name > Install import Colorgram
import colorgram

# TODO 2: Import Random, Turtle and Screen Package
from turtle import Turtle, Screen
import random

# TODO 3: Initialize Screen
screen = Screen()

# TODO 4: Set colormode to 255
screen.colormode(255)

# TODO 5: Extract the colors using Colorgram package
colors = colorgram.extract('image.jpg', 30)


# TODO 6: Extracted colors must be appended as new tuple to a list of colors.
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = [r, g, b]
    color_list.append(new_color)


# TODO 7: Initialize Turtle
timmy = Turtle()
timmy.shape('circle')

# TODO 8: Hide the turtle
timmy.hideturtle()

# TODO 9: This determines the size of the line/dot
timmy.pensize(20)

# How much the turtle is moving forward
movement = 40
y_position = -100

# How many dots/circles per row
points = 10

# The dots/circles per row are the same as the points.
# This is so, we can have a condition that subtracts from points for each iteration,
# without changing max-rows at each run.
max_rows = points

# TODO 10: Make a function for the movement of the turtle.
# def move_timmy():
#     random_color = random.choice(color_list)
#     timmy.color(random_color)
#     timmy.pendown()
#     timmy.forward(0)
#     timmy.penup()
#     timmy.forward(movement)


# TODO 11: Move the turtle using the function, then move the turtle up a row, and start the printing process again.
# while max_rows != 0:
#     for _ in range(points):
#         timmy.speed(0.51)
#         move_timmy()
#     max_rows -= 1
#     y_position += movement
#     timmy.speed('fastest')
#     timmy.goto(0, y_position)

# TODO 12: USING the turtle.dot
timmy.penup()
timmy.goto(-200, -100)
timmy.pendown()
while max_rows != 0:
    for _ in range(points):
        random_color = random.choice(color_list)
        timmy.dot(20, random_color)
        timmy.penup()
        timmy.forward(50)
    max_rows -= 1
    y_position += movement
    timmy.speed('fastest')
    timmy.goto(-200, y_position)


# TODO 3.1: Ensure that screen is only exited on click.
screen.exitonclick()