import turtle as t
from turtle import *
# tim = t that represent a module

tim = t.Turtle()
# import heroes need to check

"""Turtle Challenge - Draw a Dashed Line"""
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()






