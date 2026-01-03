import random
#step2: Replacing blanks with guesses
# todo:1:step1: randomly choose the word from word_list and assign it to a variable called chosen_word. then print it.
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#testing code
print(f"the solution is: {chosen_word}")

# todo:2:step1: ask the user to guess a letter and assign their answer to a variable called guess.make guess lower case.
guess = input("Guess a letter: ").lower()
print(guess)

#==========================================step2: replacing blanks with guess:======================================#
#todo:1 : create a "placeholder" with same number of blanks as the chosen_word
print("checking blanks as same no.of.blanks as the chosen word")
print(chosen_word)
place_holder = ""
word_length = len(chosen_word)
for position in range(word_length): # i give iteration name as position instead of letter
    place_holder += "_"
print(place_holder)

#todo:2 : create a "display" that puts the guess letters in right position and _ in the rest of the string.
# ex apple: _____ / guess letter p: _pp__   print display.
display = ""
for letter in chosen_word: # a,a,r,d,v,a,r,k  in  aardvark
    if letter == guess:  #each letter check == guess letter(usr i/p). if yes
        display += letter # add letter to display as string
    else:
        display += "_"  # no., add blanks to display
print(display)


