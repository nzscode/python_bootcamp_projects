import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Naming Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def click_coords(x, y):
    print(x, y)


turtle.onscreenclick(click_coords)

turtle.mainloop()

screen.exitonclick()