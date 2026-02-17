#understanding Turtle Graphics
from turtle import Turtle,Screen

# this one is general method
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

#another short using for loop

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()