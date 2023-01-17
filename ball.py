from turtle import Turtle
import random

STRETCH_FACTOR = 1
ANGLES = [45, 135, 225, 315]
CORNERS = [[350, 250], [-350, 250], [-350, -350], [350, -350]]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_FACTOR, stretch_len=STRETCH_FACTOR)
        self.penup()


    def move_ball(self):
        # new_angle = random.choice(ANGLES)
        # if new_angle in ANGLES:
        #     angle_index = ANGLES.index(new_angle)
        #     new_corner = CORNERS[angle_index]
        #     print(new_corner)
        #     self.setheading(new_angle)
        #     self.goto(new_corner[0], new_corner[1])
        #     self.speed(0.1)
        self.speed("slowest")
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
            