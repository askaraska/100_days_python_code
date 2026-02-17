import turtle as t
import random
tim = t.Turtle()
# total angle 360degree 360/4 means 90
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
"""Single shape draw"""
# num_sides = 5
# for side in range(num_sides): # 5 means pentagon, 3 means triangle
#     angle = 360 / num_sides
#     tim.forward(100) # go forward to 100
#     tim.right(angle) # turn right based on angles


"""Different shapes"""
def draw_shape(num_sides):
    angle = 360 / num_sides # put initial to calculate side
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# need another loop. this loop go through all the different no.of.side
for shape_side_n in range(3,11): # start from triangle to pentagon
    draw_shape(shape_side_n)
    tim.color(random.choice(colours))


screen = t.Screen()
screen.exitonclick()