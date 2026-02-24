from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off animation in screen

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen() # screen listen keystroke
screen.onkey(r_paddle.go_up , "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up , "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    # ball width 20px,paddle width 20px
    #if distance between two of them is less than 20,probably made contact
    # actual measures center of paddle and ball, ball.distance(paddle)
    # our requirement ball hit any edge of the paddle

    # # detect collision with right paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    #     ball.bounce_x()

    # # detect collision with right paddle
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    #     ball.bounce_x()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """Detect if the ball goes out of the bounds at the edge of the screen
    if yes,reset the ball position to centre of the screen
    then ball should then start moving towards the other player"""

    #detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
