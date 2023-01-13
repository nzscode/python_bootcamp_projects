from turtle import Screen
from scoreboard import Scoreboard
from midline import Midline
from paddles import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=400)

scoreboard_right = Scoreboard()
scoreboard_right.goto(100, 0)
midline = Midline()
midline.midline_dash()
screen.listen()
paddle_left = Paddle()
paddle_left.paddle_left()
paddle_right = Paddle()
paddle_right.paddle_right()
ball = Ball()
game_on = True

screen.onkey(paddle_left.paddle_left_up, "w")
screen.onkey(paddle_left.paddle_left_down, "s")
screen.onkey(paddle_right.paddle_right_up, "Up")
screen.onkey(paddle_right.paddle_right_down, "Down")

# while game_on:
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
