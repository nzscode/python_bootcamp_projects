from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.wrong_answers = 0
        self.goto(0, 350)
        self.write(f"Score: {self.score}/50 Wrong Answers: {self.wrong_answers}/10",
                   align="center", font=("Courier", 30, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}/50 Wrong Answers: {self.wrong_answers}/10",
                   align="center", font=("Courier", 30, "bold"))
