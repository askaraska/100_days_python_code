from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = [] # start with empty list
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """ Method creates a RANDOM CAR somewhere along y-axis
            This function creates a new car and adds it to the list"""
        random_chance = random.randint(1, 6) # before cae more messy
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2) # dimension of turtle
            new_car.penup() # not going to draw
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250) # gives good space for all
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
