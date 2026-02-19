from turtle import Turtle, Screen


tim = Turtle()
#in order to start listening for events,
# we have to get hold of the screen object
# & then tell it to start listening
screen = Screen()
def move_forwards():
    tim.forward(10)

screen.listen()
#once start we have to bind a function that will be trigerd, when a particular key is pressesd.
screen.onkey(key="space", fun=move_forwards) # in here don't write move_forwards()
screen.exitonclick()

"""Function as Inputs"""
#def function_a(something):
    #do something

# def function_b(something):
    #do this
    #do something

#function_a()
"""In function Calling we have to pass parameter
    in that parameter if we pass the function as a input means
    we only pass name without parameter at a end."""
#function_a(function_b):

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calculate(n1, n2, func): # In parameter 3 function as a input
    return func(n1, n2) # returns function and its have inputs

result1 = calculate(2,3,add)
print(result1)

result2 = calculate(2,3,subtract)
print(result2)

# function work with other function , concept is known as Higher Order Function