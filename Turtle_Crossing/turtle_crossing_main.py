import time
from turtle import Screen
from Turtle_Crossing.player import Player
from Turtle_Crossing.car_manager import CarManager
from Snake_Game_With_High_Score.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_level()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()