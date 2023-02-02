import turtle
from turtle import Turtle, Screen
from scoreboard import Scoreboard
import pandas

screen = Screen()
screen.title("U.S. States Naming Game")


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
data = pandas.read_csv("50_states.csv")
state_name_list = data["state"].to_list()
input_list = []
new_turtle = Turtle()
new_turtle.hideturtle()
new_turtle.penup()


game_over = False


def game():
    answer_state = screen.textinput("State Input: ", "Name a State: ").lower()
    proper_case_state = answer_state.title()
    state = data[data.state == proper_case_state]
    new_x = state.x
    new_y = state.y

    if proper_case_state in state_name_list:
        if proper_case_state not in input_list:
            new_turtle.goto(float(new_x), float(new_y))
            new_turtle.write(proper_case_state, font=("Courier", 8, "bold"))
            scoreboard.score += 1
            scoreboard.update_scoreboard()
            input_list.append(proper_case_state)
        elif proper_case_state in input_list:
            pass
    else:
        scoreboard.wrong_answers += 1
        scoreboard.update_scoreboard()
    game()


while not game_over:
    game()
    if scoreboard.score == 50 | scoreboard.wrong_answers == 10:
        game_over = True


screen.exitonclick()
