from multiprocessing.resource_sharer import stop
from turtle import Turtle, Screen
from pambu import Snake
from unavu import Food
from mathippen import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Askar Snake Game")
screen.tracer(0) # off just a screen,nothing will happen until update

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen() # screen is now listening for keystrokes
screen.onkey(snake.up, "Up") # onkey up it execute up function in Snake class
screen.onkey(snake.down, "Down") #270
screen.onkey(snake.left, "Left") #180
screen.onkey(snake.right, "Right") #0

game_is_on = True
while game_is_on:
    screen.update() #to explicitly refresh the visual output on the display.
    time.sleep(0.1)

    snake.move()
    #detect collision with food
    #Return the distance from the turtle to (x,y),
    # the given vector, or the given other turtle, in turtle step units.
    # snake segment of each is 20x20, food is certain pixel less than it takes food.
    if snake.head.distance(food) < 15: # if distance from the snake's head to the food.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    #if head collides with any segment in the tail:
    # trigger game_over
    #for segment in snake.segments:
    # for segment in snake.segments[1:]: # slicing from index 1 (starts from below snake head)
        # if snake.head.distance(segment) < 10:
            # snake head has a distance less than 10 with any of those segment
            # that's collision occurs with snake head with his segment
            # game_is_on = False
            # scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
                pass
        elif snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

# tail follow where the head is going