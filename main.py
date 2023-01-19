import time
from turtle import Screen
from scoreboard import ScoreboardRight, ScoreboardLeft
from midline import Midline
from paddles import Paddle
from ball import Ball
from bounce_borders import Border

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

scoreboard_right = ScoreboardRight()
scoreboard_left = ScoreboardLeft()
midline = Midline()
midline.midline_dash()
border_top = Border(-395, 298, 395, 298)
border_bottom = Border(-395, -290, 395, -290)
screen.listen()
paddle_left = Paddle()
paddle_left.paddle_start_position(-350, 0)
paddle_right = Paddle()
paddle_right.paddle_start_position(350, 0)
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
    if paddle_left.distance(ball) > 5 and ball.xcor() > 300 and ball.ycor() < 250 or ball.ycor() > -250:
        scoreboard_left.score += 1
    elif paddle_right.distance(ball) > 5 and ball.xcor() > -300 and ball.ycor() < 250 or ball.ycor() > -250:
        scoreboard_right.score += 1

    if ball.ycor() > 298 and ball.xcor() > 0:
        ball.setheading(275)
        ball.move_ball()

screen.exitonclick()
