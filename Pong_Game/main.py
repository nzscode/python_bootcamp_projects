import time
from turtle import Screen
from Pong_Game.scoreboard import Scoreboard
from Pong_Game.midline import Midline
from Pong_Game.paddles import Paddle
from Pong_Game.ball import Ball
import random

ANGLES = [45, 135, 225, 315]
new_angle = random.choice(ANGLES)
move_speed = 0.1

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

scoreboard_right = Scoreboard()
scoreboard_left = Scoreboard()
scoreboard_left.set_up(-75, 200)
scoreboard_right.set_up(30, 200)
scoreboard_left.update_scoreboard()
scoreboard_right.update_scoreboard()
midline = Midline()
midline.midline_dash()
screen.listen()
paddle_left = Paddle()
paddle_left.paddle_start_position(-380, 0)
paddle_right = Paddle()
paddle_right.paddle_start_position(380, 0)
ball = Ball()
game_on = True

screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")
screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_right.paddle_down, "Down")


while game_on:
    time.sleep(move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        move_speed /= 1.5

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_left.increase_score()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard_right.increase_score()


screen.exitonclick()
