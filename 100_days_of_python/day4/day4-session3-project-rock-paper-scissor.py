import random
from multiprocessing.process import parent_process

rock =         '''_______
              ---'   ____)
                   (_____)
                   (_____)
                    (____)
             ---.__(___)'''


paper =  '''   _______
           ---'   ____)____
                     ______)
                     _______)
                    _______)
           ---.__________)
           
         '''

scissors = '''  _______
            ---'   ____)____
                       ______)
                      __________)
                    (____)
            ---.__(___) 
            
            '''


game_images = [rock, paper, scissors]
# Rules of Rock Paper Scissors
# Rock crushes Scissors
# Scissors cuts Paper
# Paper covers Rock
print("welcome to the game: Rock, Paper, Scissors")
print("user choice: ")
user_choice = int(input("what do you choose? : 0 - rock, 1 - paper, 2 - scissors.\n"))
# over all possible range,game image by user
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice]) # store value like : game_images[0],game_images[1],game_images[2],
                # and we print game images
# over all possible range,game image by computer choice
print("computer choice")
computer_choice = random.randint(0,2)
print(computer_choice)
print(game_images[computer_choice])
if user_choice < 0 or user_choice > 2:
    print("invalid choice.you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win!. Rock crushes Scissors")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!. COMRock crushes Scissors")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a tie!")