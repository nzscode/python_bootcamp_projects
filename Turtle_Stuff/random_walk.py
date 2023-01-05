import random
from turtle import Turtle, Screen
screen = Screen()
timmy = Turtle()
screen.colormode(255)

directions = [0, 90, 180, 270]


def random_walk():
    timmy.shape('turtle')
    timmy.pensize(10)
    max_segments = 400
    segment_steps = 20
    random_direction = random.choice(directions)
    for _ in range(max_segments):
        timmy.speed("fastest")
        color_r = random.randint(0, 255)
        color_g = random.randint(0, 255)
        color_b = random.randint(0, 255)
        timmy.color(color_r, color_g, color_b)
        timmy.pendown()
        timmy.forward(segment_steps)
        timmy.setheading(random_direction)
        random_walk()


random_walk()

screen.exitonclick()
