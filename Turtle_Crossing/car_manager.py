from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 6:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y_pos = random.randint(-200, 200)
            new_car.goto(300, random_y_pos)
            self.cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

