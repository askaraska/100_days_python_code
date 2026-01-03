alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a different function called 'decrypt' that takes the 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text,shift_amount):
#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#e.g.
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
    plain_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)  # for ex: 'z' message, index of z is 25: "25%26" = 1 ==> alphabet[1] = b
        plain_text += alphabet[shifted_position]
    print(f"here is decoded result: {plain_text}")
decrypt(original_text=text,shift_amount=shift)
#now we have to combine encrypt() and decrypt()
#todo:3 create caesar() use value of the user 'direction' variable to determine which functionality going to use
