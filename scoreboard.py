from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("snake_high_score.txt") as data:
            self.highscore = int(data.read())
        print(self.highscore)
        self.goto(0, 250)
        self.color("white")

    def increase_score(self): 
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake_high_score.txt", mode="w") as new_high_score:
                new_high_score.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

