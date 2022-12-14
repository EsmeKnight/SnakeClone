from turtle import Turtle, Screen, penup

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # init generates snake
    def __init__(self):
        self.segments = []
        self.create_snake()
        # assigns first segment as head
        self.head = self.segments[0]

    # called in init
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # called by extend. appends another turtle to end of self.segments list
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    # called when food eaten in main
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # moves snake forward relative to heading
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # direction functions called on keypress in main.py
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

    # collision functions called in main.py. sends turtle to opposite side of screen
    def right_collision(self):
        self.head.goto(x=self.head.xcor() - 600, y=self.head.ycor())

    def left_collision(self):
        self.head.goto(x=300, y=self.head.ycor())

    def top_collision(self):
        self.head.goto(x=self.head.xcor(), y=self.head.ycor() - 600)

    def bottom_collision(self):
        self.head.goto(x=self.head.xcor(), y=300)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.goto(0, 0)
