from operator import index
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
#TODO-1: Create a function called 'encrypt' that takes the 'original_text' and 'shift_amount' as inputs.
def encrypt(original_text, shift_amount):
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet) # for ex: 'z' message, index of z is 25: "25%26" = 1 ==> alphabet[1] = b
        cipher_text += alphabet[shifted_position]
    print(f"here is encoded result: {cipher_text}")
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(original_text=text,shift_amount=shift)
##🐛Bug alert: What happens if you try to encode the word 'civilization', or z?🐛
# by using modulo, we fix this bug line no:17

