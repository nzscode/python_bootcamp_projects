from turtle import Turtle, Screen
from car import Car
from scoreboard import Scoreboard
from player import Player
import time

game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = Car()
car.car_start_position(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.player_move, "Up")

while game_on:
    screen.update()
    time.sleep(0.01)
    car.car_move()

    if player.ycor() > 250:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        player.player_reset()

screen.exitonclick()
