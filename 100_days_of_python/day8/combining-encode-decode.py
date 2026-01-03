alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


#todo:3 create caesar() use value of the user 'direction' variable to determine which functionality going to use
def caesar(original_text,shift_amount,encode_or_decode):
    plain_text = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter)  + shift_amount
        shifted_position %= len(alphabet)
        plain_text += alphabet[shifted_position]
    print(f"here is {encode_or_decode}d result: {plain_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    further_continue = input("if you want to continue type 'yes' or else 'no':\n").lower()
    if further_continue == "no":
        should_continue = False
        print("Goodbye!")


