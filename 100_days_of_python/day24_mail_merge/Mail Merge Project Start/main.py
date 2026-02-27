#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]" # creating constant .. in letter have dear name future change need

# open invited_names.txt file in Names back in Input
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # names in invited_names files are in turn into list
    print(names)

# open starting_letter.txt file in Letters back in Input
with open("./Input/Letters/starting_letter.txt") as letters_file:
    letter_contents = letters_file.read()
    # print(letters_contents)
    for name in names: # loop names in invited_names list on this part
        stripped_name = name.strip()  # stores names with stripped
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # instead of using name use stripped_name
        print(new_letter)
        # creating text file for each names which has stripped
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)