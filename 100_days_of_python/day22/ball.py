from turtle import Turtle

class Ball(Turtle):
    """ when initiate ball object, default attribute """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """ball moving x and y by 10 . that's on the default attribute"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 # opposite act of y-axis, + means -, - means +

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 # when hit paddle it increases speed from default value to as per given value

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x() # opposite chance
