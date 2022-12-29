from turtle import Turtle, Screen

shape_sides = int(input("How many sides to the shape?  \n"))
shape_steps = int(input("How many steps per side?   \n"))
shape_angle = 360/shape_sides
new_angle = 0

timmy = Turtle()
timmy.shape('turtle')
timmy.color("green")
timmy.speed(0.51)
remaining_steps = shape_steps
dash_length = 4
dash_segments = 25
for i in range(shape_sides):
    for x in range(dash_segments):
        timmy.pendown()
        timmy.forward(dash_length)
        remaining_steps -= dash_length
        timmy.penup()
        timmy.forward(dash_length)
        remaining_steps -= dash_length
        dash_segments -= 2
    new_angle += shape_angle
    timmy.setheading(new_angle)
screen = Screen()
screen.exitonclick()


