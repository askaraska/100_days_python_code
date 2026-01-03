def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#hurdle no:3 position & no.of hurdles changes each time,flag destination not known.
#need to know: move(),turn_left(),turn_right(),jump().,
#condition: at_goal(),wall_in_front
#logic: stop when reaches goal, if wall in front jump, 
#need to modify jump(),need to turn robot 1st for jump

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_wall = 0    
while not at_goal():
    if wall_in_front():
        number_of_wall += 1
        jump()
    else:
        move()
print(number_of_wall)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
