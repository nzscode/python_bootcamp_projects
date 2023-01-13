from turtle import Turtle, Screen
STARTING_POSITIONS = [[0, 0], [-20, 0], [-40, 0]]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.snake()
        self.head = self.snake_segments[0]

    def snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_index in range(len(self.snake_segments) - 1, 0, -1):
            previous_seg_x = self.snake_segments[seg_index - 1].xcor()
            previous_seg_y = self.snake_segments[seg_index - 1].ycor()
            self.snake_segments[seg_index].setposition(previous_seg_x, previous_seg_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
