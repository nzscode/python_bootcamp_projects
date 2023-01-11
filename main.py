import time
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakeyyyyy")
screen.tracer(0)


snake_segments = []

for _ in range(3):
    new_segment = Turtle()
    new_segment.penup()
    new_segment.color("white")
    new_segment.shape("square")
    new_segment.speed("fastest")
    x_pos = -20 * len(snake_segments)
    new_segment.setposition(x_pos, 0)
    snake_segments.append(new_segment)

game_over = False


def left():
    new_heading = snake_segments[0].heading() + 90
    snake_segments[0].setheading(new_heading)


def right():
    new_heading = snake_segments[0].heading() - 90
    snake_segments[0].setheading(new_heading)


while not game_over:
    screen.update()
    time.sleep(0.1)
    for seg_index in range(len(snake_segments) - 1, 0, -1):
        previous_seg_x = snake_segments[seg_index - 1].xcor()
        previous_seg_y = snake_segments[seg_index - 1].ycor()
        snake_segments[seg_index].setposition(previous_seg_x, previous_seg_y)

    screen.listen()
    snake_segments[0].forward(20)

    screen.onkey(left, "a")
    screen.onkey(right, "d")
















screen.exitonclick()
