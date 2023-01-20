from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(0, 250)
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()

    def update_scoreboard(self):
        self.write(f"{self.score}")
