def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
#completion of one hurdle:
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#need to jump six times for complete hurdle 1:
#can do jump() six times or for loop:
#for completing entire hurdle 1 challenge flag reach

for step in range(6):
    jump()





################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
