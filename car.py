from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.shape("square")
        self.penup()
        self.setposition(250, 0)
        self.showturtle()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def car_move(self):
        self.backward(5)

    def car_start_position(self, y_pos):
        self.setposition(250, y_pos)
        self.showturtle()


