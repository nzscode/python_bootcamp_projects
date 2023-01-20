from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.setposition(0, -250)
        self.showturtle()

    def player_move(self):
        self.forward(20)

    def player_reset(self):
        self.goto(0, -250)
