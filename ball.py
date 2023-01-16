from turtle import Turtle
import random

STRETCH_FACTOR = 1
ANGLES = [45, 135, 225, 315]
CORNERS = [[350, 350], [-350, 350], [-350, -350], [350, -350]]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_FACTOR, stretch_len=STRETCH_FACTOR)
        self.penup()

    def start_angle(self):
        for angle in ANGLES:
            