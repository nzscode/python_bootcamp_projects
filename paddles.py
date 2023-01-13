from turtle import Turtle
UP = 90


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(UP)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed("slow")

    def paddle_left(self):
        self.goto(-300, 0)

    def paddle_right(self):
        self.goto(300, 0)

    def paddle_left_up(self):
        self.goto(-300, 300)

    def paddle_left_down(self):
        self.goto(-300, -300)

    def paddle_right_up(self):
        self.goto(300, 300)

    def paddle_right_down(self):
        self.goto(300, -300)
