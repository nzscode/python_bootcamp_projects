from turtle import Turtle, Screen

shape_sides = int(input("How many sides to the shape?  \n"))
shape_steps = int(input("How many steps per side?   \n"))
shape_angle = 360/shape_sides
new_angle = 0
timmy = Turtle()
timmy.shape('turtle')
timmy.color("green")
timmy.speed(0.51)
timmy.pendown()
for i in range(shape_sides):
    timmy.forward(shape_steps)
    new_angle += shape_angle
    timmy.setheading(new_angle)
screen = Screen()
screen.exitonclick()


