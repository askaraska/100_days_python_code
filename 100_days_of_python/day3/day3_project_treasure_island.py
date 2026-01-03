print("welcome to the treasure island")
print("your mission is to find the treasure")
road_choice1 = input('you\'re at a crossroad, where do you want to go?'
                     'type "Left" or "Right".\n').lower()
if road_choice1 == 'left':
    lake_choice2 = input('you\'ve come to a lake_choice2\n'
                        'there is a island in middle of the lake_choice2\n'
                        'type "wait" for a boat\n'
                        'type "swim" to swim across the lake.\n').lower()
    if lake_choice2 == 'wait':
        color_door_choice3 = input('you arrive at a unharmed_island.\n'
                                        "there is house with three doors.\n" 
                                        "one red,one yellow and one blue.\n"
                                        "which colour do you choose\n").lower()
        if color_door_choice3 == "red":
            print("game over.room full of fire")
        elif color_door_choice3 == "yellow":
            print("you found the treasure. you win!")
        elif color_door_choice3 == "blue":
            print("room of beasts. game over!")
        else:
            print("door doesn't exists game over")
    else:
        print("you are attacked by angry trout. game over!.")
else:
    print("you fell into a hole.game over!.")
