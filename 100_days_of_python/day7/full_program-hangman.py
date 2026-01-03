import random
#step:5 improving ux: adding ascii art and the ui.
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
#TODO-2: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_ascii import stages
from hangman_ascii import logo
"""we choose word randomly from word_list and store to the variable chosen_word"""
chosen_word = random.choice(word_list)
# checking chosen_word length and store to a word_length variable
word_length = len(chosen_word)
correct_letters = [] # empty list created for storing correct letters  which are guessed
game_over = False
#Set 'lives' to equal 6.
lives = 6

"""from here start of hangman game"""
# print start of game
print(logo)

#Testing code
print("computer chosen word: ",chosen_word)

print("checking blanks as same no.of.blanks as the chosen word")

#create a "placeholder" with empty string
# and check there is same number of blanks as the chosen_word
place_holder = ""
for position in range(word_length): #  we iterate through word_length ex: word:camel - word_length is 5 - range 0 to 4.
    place_holder += "_"
print("Word to guess: " + place_holder)

# use a while loop to let the user guess again and again, loop should only stop when user guessed all letter in chosen_word.
while not game_over: # not game over means, while condition execute
    #todo:5 update the code below to tell user how many lives they have left
    print(f"********{lives}/6 lives left********")
    guess = input("Guess a letter: ").lower()  #execute statement, that are user i/p again and again

    display = ""      # create a display variable in right place in code. give inside while loop
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"you've already guessed {guess}.!")
    for letter in chosen_word: # a,a,r,d,v,a,r,k  in  aardvark
        if letter == guess:  #each letter check == guess letter(usr i/p). if yes
            display += letter # add letter to display variable as string
            correct_letters.append(guess) # and all correct guessed letter are append to correct_letters[].
        elif letter in correct_letters: #in list of correct_letters[]
            display += letter # added to a variable display
        else:
            display += "_"  # no., add blanks to display
    print("The word to guess is: " + display)

    #  If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"you guessed {guess} not in word. you lose life.")
        if lives == 0:
            game_over = True
            print(f"******It Was {chosen_word}!. You lose.*******")
    # Check if user has got all letters.
    if "_" not in display:
        game_over = True
        print("******you win!*******")
    print(stages[lives]) # give stage print in right place inside while loop and same line of for, 1st if.