#escaping maze:with zipped file problem of game
#if,elif,else..
#secret is to have reeborg follow a long the right edge of the maze,turning right if it can.
#go straight ahead if can't turn right, or turning left as a last resort.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#step1:every time when the robot side is clear turn right() and move()
#check to see if it is at the goal. so, it's not and again if right side is clear turnright and moves
#step2: create another while loop before this while loop runs
while front_is_clear():
    move()
#step3: move untill it's hit a wall in front. so, need to turn_left when hits a wall
turn_left()
#step4: create another while loop and check condition:
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# ok for 1st file but for 2nd file this code become infinte loop.
#to be continued.....


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
