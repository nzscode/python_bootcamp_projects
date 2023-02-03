import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Naming Game")


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("US_States_Naming_Game/50_states.csv")
state_name_list = data["state"].to_list()
input_list = []
new_turtle = Turtle()
new_turtle.hideturtle()
new_turtle.penup()
scoreboard = Turtle()
scoreboard.penup()
scoreboard.hideturtle()
score = 0
wrong_answers = 0
scoreboard.goto(0, 350)
scoreboard.write(f"Score: {score}/50 Wrong Answers: {wrong_answers}/10", align="center", font=("Courier", 30, "bold"))

game_over = False


while not game_over:
    answer_state = screen.textinput("State Input: ", "Name a State: ").lower()
    trimmed_state = answer_state.strip()
    proper_case_state = trimmed_state.title()
    state = data[data.state == proper_case_state]
    new_x = state.x
    new_y = state.y

    if proper_case_state in state_name_list:
        if proper_case_state not in input_list:
            new_turtle.goto(float(new_x), float(new_y))
            new_turtle.write(proper_case_state, font=("Courier", 8, "bold"))
            score += 1
            input_list.append(proper_case_state)
            scoreboard.clear()
            scoreboard.write(f"Score: {score}/50 Wrong Answers: {wrong_answers}/10",
                             align="center", font=("Courier", 30, "bold"))
        elif proper_case_state in input_list:
            pass
    else:
        wrong_answers += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}/50 Wrong Answers: {wrong_answers}/10",
                         align="center", font=("Courier", 30, "bold"))

    if wrong_answers > 10:
        for state in data.state:
            if state not in input_list:
                final_turtle = Turtle()
                final_turtle.penup()
                final_turtle.hideturtle()
                missing_state = data[data.state == state]
                final_turtle.goto(float(missing_state.x), float(missing_state.y))
                final_turtle.write(state, font=("Courier", 8, "bold"))
                game_over = True


screen.exitonclick()
