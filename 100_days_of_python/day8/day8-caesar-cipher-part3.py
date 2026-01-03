#===================REORGANIZING CODE===========================#
#todo1: import and print tje logo from art.py when program starts
from art import logo
print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
#create caesar() use value of the user 'direction' variable to determine which functionality going to use
def caesar(original_text,shift_amount,encode_or_decode):
    plain_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            plain_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            plain_text += alphabet[shifted_position]
    print(f"here is {encode_or_decode}d result: {plain_text}")

#todo:2 what happens if user enters a number/symbol/space? in line no :15

#todo:3 can you figure out a way to restart the cipher program

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) # caesar calling fn should give after while loop
    restart = input("Type 'yes' if you want to go again. otherwise, type 'no':\n ").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
