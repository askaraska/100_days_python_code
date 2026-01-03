import random
#step1
#todo:1: randomly choose the word from word_list and assign it to a variable called chosen_word. then print it.
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo:2: ask the user to guess a letter and assign their answer to a variable called guess. make guess lower case.
guess = input("Guess a letter: ").lower()
print(guess)

#todo:3: check if the letter the user guessed(guess) is one of the letter in chosen_word. print "right", if it is wrong print "wrong".
# for letter in chosen_word:
#     print(letter)  == instead of printing letter we want to check to see if the letter same as guess letter.

for letter in chosen_word: #for letter in camel chosen_word: c,a,m,e,l
    if letter == guess:  # c,a,m,e,l == guess(usr i/p)
        print("right")  # a is right
    else:
        print("wrong") # c,m,e,l is wrong o/p is printed..
print(f"the word is: {chosen_word}.")




