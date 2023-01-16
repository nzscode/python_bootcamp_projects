from turtle import Turtle

DASH_LENGTH = 10


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.color("white")
        self.speed("fastest")
        self.pensize(5)

    def midline_dash(self):
        for pace in range(40):
            self.setheading(90)
            self.pendown()
            self.forward(DASH_LENGTH)
            self.penup()
            self.forward(DASH_LENGTH + 2)
