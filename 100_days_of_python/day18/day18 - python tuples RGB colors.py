my_tuple = (1,3,8)
print(my_tuple[2]) #o/p: 8
# my_tuple[2] = 12  # ERROR

import turtle as t
import random
tim = t.Turtle()

#cmode – one of the values 1.0 or 255
#Return the colormode or set it to 1.0 or 255.
#Subsequently r, g, b values of color triples have to be in the range 0..*cmode*."""
t.colormode(255)

"""Return color of RGB by using 0 to 255 values"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b) # (253,157,24)
    return rand_color

directions = [0,90,180,270]
tim.speed("fastest")
tim.pensize(15)

for _ in range(200):
    tim.color(random_color())
    tim.forward(100)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()