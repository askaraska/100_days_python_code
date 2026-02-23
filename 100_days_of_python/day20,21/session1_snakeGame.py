from multiprocessing.resource_sharer import stop
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Askar Snake Game")

"""Challenge: Create 3 turtles and position them like
              Each turtle should be a white square 20x20
              Normal creation of turtle it would be centre point 3 in 1"""

# segment1 = Turtle("square")
# segment1.color("white")
#
# segment2 = Turtle("square")
# segment2.color("white")
# segment2.goto(x=-20, y=0) # square turtle come left from centre based on graph
#
# segment3 = Turtle("square")
# segment3.color("white")
# segment3.goto(x=-40, y=0)

# another method of creation 3square turtle by using for loop
starting_positions = [(0, 0),(-20, 0),(-40, 0)]
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()