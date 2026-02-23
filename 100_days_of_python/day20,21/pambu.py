from turtle import Turtle
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self): # when our obj initialize what are things start with
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # indicates head of the snake, takes from self.segments list

    """Create Three Segment Snake using the Starting Positions"""
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # protect from drawing
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # 3rd goto 2nd, 2nd goto 1
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # self.segments[0].setheading(90)

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # when snake head point towards down direction, not allow to up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)