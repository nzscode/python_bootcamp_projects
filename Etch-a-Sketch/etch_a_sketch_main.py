from turtle import Turtle, Screen
import random
screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.pensize(8)
screen.colormode(255)
color_r = random.randint(0, 255)
color_b = random.randint(0, 255)
color_g = random.randint(0, 255)
tim.color(color_r, color_g, color_b)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


# def counter_clockwise():
#     tim.circle(0, 15, 1)
#
# def clockwise():
#     tim.circle(-0.01, 15, 1)

def turn_left():
    new_heading = tim.heading() + 5
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 5
    tim.setheading(new_heading)


def clear_reset():
    tim.reset()


screen.listen()
screen.onkey(move_backward, "s")
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_reset, "c")



screen.exitonclick()