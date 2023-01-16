from turtle import Screen
from scoreboard import ScoreboardRight,ScoreboardLeft
from midline import Midline
from paddles import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

scoreboard_right = ScoreboardRight()
scoreboard_left = ScoreboardLeft()
midline = Midline()
midline.midline_dash()
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
    screen.update()
    screen.onkey(ball.start_angle, "c")

#     ball_position = [ball.xcor(), ball.ycor()]
#     if ball.xcor() < -300:
#         scoreboard_left.score += 1
#         game_on = False
#     elif ball.xcor() > 300:
#         scoreboard_right.score += 1
#         game_on = False
#     elif ball.distance(paddle_left) < 5 or ball.distance(paddle_right) < 5:
#         pass
#         #ball bounces back




screen.exitonclick()
