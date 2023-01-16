from turtle import Turtle
UP = 90
MOVE_STEPS = 100
STRETCH_WIDTH = 1
STRETCH_LENGTH = 5
MAX_Y = 240
MIN_Y = -225


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(UP)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        self.speed("slow")

    def paddle_start_position(self, pos_x, pos_y):
        self.goto(pos_x, pos_y)

    def paddle_up(self):
        if self.ycor() < MAX_Y:
            self.forward(MOVE_STEPS)

    def paddle_down(self):
        if self.ycor() > MIN_Y:
            self.backward(MOVE_STEPS)

