from turtle import Turtle
import random

NEG_LIMIT = -250 + 20
POS_LIMIT = 250 - 20

STRETCH_RATIO = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=STRETCH_RATIO, stretch_wid=STRETCH_RATIO)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        location_x = random.randint(NEG_LIMIT, POS_LIMIT)
        location_y = random.randint(NEG_LIMIT, POS_LIMIT)
        self.goto(location_x, location_y)