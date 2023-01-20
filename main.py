import time
from turtle import Screen
from scoreboard import Scoreboard
from midline import Midline
from paddles import Paddle
from ball import Ball
import random

ANGLES = [45, 135, 225, 315]
new_angle = random.choice(ANGLES)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

scoreboard_right = Scoreboard()
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
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 340 or ball.distance(paddle_left) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()
