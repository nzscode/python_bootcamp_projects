import random
from turtle import Turtle, Screen
screen = Screen()
shape_sides = 3
    # int(input("How many sides to the shape?  \n"))
shape_steps = 25
    # int(input("How many steps per side?   \n"))


timmy = Turtle()

screen.colormode(255)


def draw_shape():
    timmy.shape('turtle')
    timmy.pensize(8)
    dash_length = 4
    seggies = shape_steps / dash_length
    dash_segments = int(seggies)
    global shape_sides
    while shape_sides < 11:
        remaining_steps = shape_steps
        shape_angle = 360 / shape_sides
        new_angle = 0
        color_r = random.randint(0, 255)
        color_g = random.randint(0, 255)
        color_b = random.randint(0, 255)
        color_choice = (color_r, color_g, color_b)
        timmy.color(color_choice)
        for i in range(shape_sides):
            for x in range(dash_segments):
                timmy.pendown()
                timmy.forward(dash_length)
                remaining_steps -= dash_length
                timmy.penup()
                timmy.forward(dash_length * 4)
                remaining_steps -= dash_length
            new_angle += shape_angle
            timmy.setheading(new_angle)

        shape_sides += 1

    draw_shape()


draw_shape()

screen.exitonclick()
