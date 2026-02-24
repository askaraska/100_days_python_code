#width = 20,height = 100, x_pos = 350, y_pos = 0 -- right side paddle
#key press - move paddle up,down 20pixels
from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off animation in screen

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1) # streching a turtle
paddle.penup()
paddle.goto(370,0)

def go_up():
    new_y= paddle.ycor() + 20 # y_cor move up by 20
    paddle.goto(paddle.xcor(),new_y) # paddle go up by 20, x_cor remains no change

def go_down():
    new_y= paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.listen() # screen listen keystroke
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on=True
while game_is_on:
    screen.update()


screen.exitonclick()
