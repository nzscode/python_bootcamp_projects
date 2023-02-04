import turtle
from turtle import Turtle, Screen
from US_States_Naming_Game.scoreboard import Scoreboard
import pandas

screen = Screen()
screen.title("U.S. States Naming Game")
image = "US_States_Naming_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("US_States_Naming_Game/50_states.csv")
state_name_list = data["state"].to_list()
input_list = []
scoreboard = Scoreboard()
new_state_dict = {
    "state name": []
}
game_over = False


while not game_over:
    answer_state = screen.textinput("State Input: ", "Name a State: ").title()
    state = data[data.state == answer_state]

    if answer_state in state_name_list:
        if answer_state not in input_list:
            new_turtle = Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            new_turtle.goto(float(state.x), float(state.y))
            new_turtle.write(answer_state, font=("Courier", 8, "bold"))
            scoreboard.score += 1
            input_list.append(answer_state)
            scoreboard.clear()
            scoreboard.write(f"Score: {scoreboard.score}/50",
                             align="center", font=("Courier", 30, "bold"))
        elif answer_state in input_list:
            pass

    if answer_state == "Exit":
        for state in data.state:
            if state not in input_list:
                final_turtle = Turtle()
                final_turtle.hideturtle()
                final_turtle.penup()
                final_turtle.color("red")
                missing_state = data[data.state == state]
                final_turtle.goto(float(missing_state.x), float(missing_state.y))
                final_turtle.write(state, font=("Courier", 8, "bold"))
                new_state_dict["state name"].append(state)
                game_over = True


df = pandas.DataFrame(new_state_dict)
df.to_csv("missed_states.csv")

screen.exitonclick()
