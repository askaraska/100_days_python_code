def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
#completion of one hurdle_function for individual one hurdle completion:
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# using while loop complete hurdle1 challenge:

number_of_hurdles = 6
while number_of_hurdles > 0 :
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
