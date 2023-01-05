import random
from turtle import Turtle, Screen
screen = Screen()
timmy = Turtle()


def draw_spirograph():
    screen.colormode(255)
    timmy.speed("fastest")
    radius = 150
    circle_number = 150
    move_amount = 360/circle_number
    new_heading = 0 + move_amount
    for _ in range(circle_number):
        color_r = random.randint(0, 255)
        color_g = random.randint(0, 255)
        color_b = random.randint(0, 255)
        timmy.pencolor(color_r, color_g, color_b)
        timmy.circle(radius)
        timmy.setheading(new_heading)
        new_heading += move_amount


draw_spirograph()
screen.exitonclick()