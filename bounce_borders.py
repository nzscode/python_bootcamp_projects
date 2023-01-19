from turtle import Turtle


class Border(Turtle):
    def __init__(self, start_x, start_y, end_x, end_y):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(start_x, start_y)
        self.pendown()
        self.goto(end_x, end_y)
