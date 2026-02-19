from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=600) # setupthe screen size
"""Pop up a dialog window for input of a string. 
Parameter title is the title of the dialog window, 
propmt is a text mostly describing what information to input. """
user_turtle = screen.textinput(title="Make your turtle", prompt="which turtle will win the race? Enter a color:")
# print(user_turtle)
y_positions = [-100,-70,-40,-10,20,50]
colors = ["red","green","blue","yellow","orange","purple"]
for turtle_index in range(0,6): # total 6: index= 012345
    tim = Turtle(shape="turtle") #determines shape of turtle in tim obj in Turtle class
    tim.color(colors[turtle_index])  #takes from colorlist with index
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtle_index])

screen.exitonclick()