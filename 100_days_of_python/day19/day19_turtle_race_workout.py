from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=600) # setupthe screen size
"""Pop up a dialog window for input of a string. 
Parameter title is the title of the dialog window, 
propmt is a text mostly describing what information to input. """
user_turtle = screen.textinput(title="Make your turtle", prompt="which turtle will win the race? Enter a color:")
# print(user_turtle)
y_positions = [-100,-70,-40,-10,20,50]
colors = ["red","green","blue","yellow","orange","purple"]
all_turtles = []
for turtle_index in range(0,6): # total 6: index= 012345
    new_turtle = Turtle(shape="turtle") #determines shape of turtle in tim obj in Turtle class
    new_turtle.color(colors[turtle_index])  #takes from colorlist with index
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle) # append six turtle in all turtle in name of new_turtles
if user_turtle:
    is_race_on = True

while is_race_on:
    #need random number
    for turtle in all_turtles: # 6 turtles
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turcolor = turtle.pencolor()
            if winning_turcolor == user_turtle:
                print(f"You win! The {winning_turcolor} turtle is the winner!")
            else:
                print(f"You lose! The {winning_turcolor} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance) # each turtle forward by random distance



screen.exitonclick()