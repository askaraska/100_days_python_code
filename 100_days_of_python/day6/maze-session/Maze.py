#escaping maze:
#if,elif,else..
#secret is to have reeborg follow a long the right edge of the maze,turning right if it can.
#go straight ahead if can't turn right, or turning left as a last resort.

#step1: need a way to turn right:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#step2:todo things, check for thing until reaches the goal
#while loop continue working untill reaches a goal. so, while not at_goal():
#test to see if it is right side clear should turn right and go straight 
#(means moving towards right)
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
#step3: if right is not clear.,does'nt know what else to do stuck in infinite loop
#so, give alternate else, if right is not clear

# this code works good.. but sometimes not for example robot centre position it will loop
#again and again 




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
