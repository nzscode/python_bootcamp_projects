from turtle import Turtle
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(30, 200)
        self.write(f"{self.score}", font=FONT)

