def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#hurdle no:2 => does'nt know where the destination flag
#need to know: move(),turn_left(),condition: at_goal
#logic: flag reaches destination comes: 
#at_goal is true, robot reaches destination, else not yet reached flag.

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
number_of_hurdles = 0

while not at_goal():
    jump()
    number_of_hurdles += 1
    
print(number_of_hurdles)




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
