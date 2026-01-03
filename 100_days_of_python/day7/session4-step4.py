import random
#step4: keeping track of the player's lives.
stages = ['''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        '''
]

game_over = False
#randomly choose the word from word_list and assign it to a variable called chosen_word. then print it.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
correct_letters = [] # empty list created for storing correct letters  which are guessed

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
#Testing code
print("checking blanks as same no.of.blanks as the chosen word")
print(chosen_word)
#create a "placeholder" with same number of blanks as the chosen_word
place_holder = ""
for position in range(word_length): #  give iteration name as position instead of letter
    place_holder += "_"
print(place_holder)

# use a while loop to let the user guess again and again, loop should only stop when user guessed all letter in chosen_word.
while not game_over: # not game over means, while condition execute
    guess = input("Guess a letter: ").lower()  #execute statement, that are user i/p again and again
    display = ""      # create a display variable in right place in code. give inside while loop
    for letter in chosen_word: # a,a,r,d,v,a,r,k  in  aardvark
        if letter == guess:  #each letter check == guess letter(usr i/p). if yes
            display += letter # add letter to display variable as string
            correct_letters.append(guess) # and all correct guessed letter are append to correct_letters[].
        elif letter in correct_letters: # now in list of correct_letters[]
            display += letter # added to a variable display
        else:
            display += "_"  # no., add blanks to display
    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    # Check if user has got all letters.
    if "_" not in display:
        game_over = True
        print("you win!")
    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives]) # give stage print in right place inside while loop and same line of for, 1st if.