from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.score = 0
        self.write(f"Score: {self.score}/50", align=ALIGN, font=FONT)

