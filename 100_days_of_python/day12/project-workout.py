import random
import art

#I HAVE TWO GLOBAL CONSTANTS CAN USE ANY OF THESE FUNCTION ANYWHERE ON THIS PAGE
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#function to check against the actual number
def check_answer(user_guess,actual_answer,turns): # parameter with i/p of user guessing and actual answer, turns 10 or 5
    if user_guess > actual_answer:
        print("Number is too high.")
        return turns -1           #turns = 10 : return 10-1 =9 / turns = 5 : return 5-1 =4
    elif user_guess < actual_answer:
        print("Number is too low.")
        return turns -1      #turns = 10 : return 10-1 =9 / turns = 5 : return 5-1 =4
    else:
        print(f"You got it! The answer was {actual_answer}")
        return None


#function to set difficulty
def level_of_difficulty():
    level = input("Choose a difficulty level: type 'easy' or 'hard': ")
    if level == "easy":
        #after this need to make 5 or 10 attempt remaining
        #creating global constants
        return EASY_LEVEL_TURNS   #global constants easy_level_turns return 10
    else:
        return HARD_LEVEL_TURNS #setting in here no use, actually need it inside my game


#entire game function
def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"our selected answer {answer}")
    """ This line turns = level_of_difficulty() trigger function level_of_difficulty()  """
    """ In level_of_difficulty() function based on user input easy or hard it return value 5 or 10. and stored to turns  """
    turns = level_of_difficulty()  # 5 or 10 value
    guess = 0
    # repeat the guessing functionality if they get it wrong

    while guess != answer:
        # let the user guess number
        print(f"you have {turns} attempts remaining to guess the number") # show user to remaining attempt. turns shows
        guess = int(input("make a guess:"))
        """after user guessing of number need to check with actual answer
         so call check_answer() and pass parameter as well"""
        turns = check_answer(guess,answer,turns)
        #ended the program dont repeating the guess

        if turns == 0:
            print("you've run out of guesses, you lose.")
            return
        # track the number of turns and reduce by 1 if they get wrong do it check answer()
        elif guess != answer:
            print("guess again")

game()



