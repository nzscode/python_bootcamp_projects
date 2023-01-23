import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"Snake Game")
screen.tracer(0)
snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_scoreboard()
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 250 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

