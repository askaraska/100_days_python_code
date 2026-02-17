import turtle as t
import random
tim = t.Turtle()


t.colormode(255)
#cmode – one of the values 1.0 or 255
#Return the colormode or set it to 1.0 or 255.
#Subsequently r, g, b values of color triples have to be in the range 0..*cmode*."""


"""Return color of RGB by using 0 to 255 values"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")
tim.color(random_color())
tim.circle(100) # circle(radius) 50 means small circle, 100 large than 50

"""draw a two circle as """
# print(tim.heading()) # o/p: 0.0
# current_heading = tim.heading()
# tim.setheading(current_heading + 10)
# tim.circle(100)

tim.heading()
current_heading = tim.heading()

# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(current_heading + 10)
"""Function for draw the spirograph"""
def draw_spirograph(size_of_graph):# parameter takes size of the spirograph
    for _ in range(int(360/size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)

draw_spirograph(5)
# draw_spirograph(20)

screen = t.Screen()
screen.exitonclick()

