from multiprocessing.resource_sharer import stop
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Askar Snake Game")
"""The screen.tracer() function in Python's turtle module,
it takes number as input
is used to turn on/off automatic screen animations, 
allowing complex drawings to be rendered instantly."""
screen.tracer(0) # off just a screen,nothing will happen until call update

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
starting_positions = [(0, 0),(-20, 0),(-40, 0)] # 0,1,2
segments = [] # □□□ in list by new_segment
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup() # protect from drawing
    new_segment.goto(position)
    segments.append(new_segment) # □□□


game_is_on = True
while game_is_on:
    screen.update() #to explicitly refresh the visual output on the display and in program it happen when all seg has move fprward.
    time.sleep(0.1) # The Python time.sleep() function is used to pause the execution of the current thread for a specified number of seconds
    #range fn() can't execute keyword argument
    # for seg_num in range(start=2, stop=0, step =-1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor() # 3rd goto 2nd in x-axis, 2nd goto 1
        new_y = segments[seg_num-1].ycor() #3rd goto 2nd in y-axis
        segments[seg_num].goto(new_x, new_y)# last_seg goto the position of second last seg
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()

# tail follow where the head is going