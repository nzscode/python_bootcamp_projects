from turtle import Turtle
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def set_up(self, x_pos, y_pos):
        self.setposition(x_pos, y_pos)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", font=FONT)
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", font=FONT)

