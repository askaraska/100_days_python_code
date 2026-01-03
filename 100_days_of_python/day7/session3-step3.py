import random
#step3: checking if the player has won
#randomly choose the word from word_list and assign it to a variable called chosen_word. then print it.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print("checking blanks as same no.of.blanks as the chosen word")
print(chosen_word)
place_holder = ""
for position in range(word_length): #  give iteration name as position instead of letter
    place_holder += "_"
print(place_holder)


#==========================================step3: checking if the player has won======================================>
#user going to continue guessing again and again until all letter in word got executed
#todo:1  use a while loop to let the user guess again and again, loop should only stop when user guessed all letter in chosen_word.
game_over = False #step1
correct_letters = [] #step:2# empty list created for storing correct letters  which are guessed
while not game_over: # not game over means, while condition execute
    guess = input("Guess a letter: ").lower()  #execute statement, that are user i/p again and again
    display = ""
#todo:2 change for loop so that you keep previous letter in display
    for letter in chosen_word: # a,a,r,d,v,a,r,k  in  aardvark
        if letter == guess:  #each letter check == guess letter(usr i/p). if yes
            display += letter # add letter to display variable as string
            correct_letters.append(guess) # and all correct guessed letter are append to correct_letters[].
        elif letter in correct_letters: #in list of correct_letters[]
            display += letter # added to a variable display
        else:
            display += "_"  # no., add blanks to display
    print(display)
    if "_" not in display:
        game_over = True
        print("you win!")