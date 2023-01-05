import random
from turtle import Turtle, Screen
screen = Screen()
timmy = Turtle()
screen.colormode(255)

# colors = ["CornflowerBlue", "Blue", "MidnightBlue", "DeepSkyBlue", "SteelBlue", "DarkTurquoise", "DarkCyan",
#           "MediumAquamarine", "SeaGreen", "SpringGreen", "Green", "Lime", "OliveDrab", "Olive", "Goldenrod",
#           "Peru", "Firebrick", "Maroon", "Coral", "Red", "LightCoral", "IndianRed", "HotPink", "DeepPink",
#           "PaleVioletRed", "Purple", "Magenta", "Orchid", "DarkOrchid", "MediumPurple", "Indigo",
#           "MediumSlateBlue", "DarkSlateBlue"]

max_steps = 300

for _ in range(10):
    while max_steps != 0:
        # timmy.pencolor(random.choice(colors))
        color_r = random.randint(0, 255)
        color_g = random.randint(0, 255)
        color_b = random.randint(0, 255)
        timmy.color(color_r, color_g, color_b)
        timmy.pensize(8)
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(20)
        max_steps -= 20

screen.exitonclick()
