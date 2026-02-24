from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # streching a turtle
        self.penup()
        self.goto(position)
        self.go_up()
        self.go_down()

    def go_up(self):
        new_y = self.ycor() + 20  # y_cor move up by 20
        self.goto(self.xcor(), new_y)  # paddle go up by 20, x_cor remains no change

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)