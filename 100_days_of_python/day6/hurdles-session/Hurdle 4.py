def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#hurdle no:4 jumpimg over hurdles with variable heights,
#completely random: no.of.hurdles,height,falg
#need to know: move(),turn_left(),turn_right(),jump().,
#condition: front_is_clear(),at_goal(),wall_in_front,
#logic: stop when reaches goal, if wall in front going to jump more,no wall infront move
#need to turn robot left first when facing the wall. modify jump()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
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
