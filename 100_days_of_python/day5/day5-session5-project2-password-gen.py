import random
#need to create letters,numbers,symbols for password storage.
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

# hard level =
print("welcome to python password generator")
#ask user to how many latter
nos_letters = int(input("how many letters would you like in password ? :\n")) #if i enter 4 means,
# value 4 stored in nos_letters
# ask user to how many symbol
nos_symbols = int(input(f"how many symbols would you like in password ? :\n"))
# ask user to how many number
nos_numbers = int(input("how many numbers would you like in password ? :\n"))
password_list = []               # password empty list
for char in range(0,nos_letters): # take range from user inputted no.of letter: 0,1,2,3 = 4 enter via for loop
    password_list.append(random.choice(letters)) # 4 iteration happens and randomly choose 4 letters from letters list
for char in range(0,nos_symbols): # take range from user inputted no.of symbols range: 0,1,2,3 = 4 enter via for loop
    password_list.append(random.choice(symbols))  # 4 iteration happens and randomly choose 4 symbols from symbols list
for char in range(0,nos_numbers): # take range from user inputted symbols no.of  range: 0,1,2,3 = 4 enter via for loop
    password_list.append(random.choice(numbers)) # 4 iteration happens and randomly choose 4 numbers from numbers list
print(password_list)
random.shuffle(password_list)
print(password_list)
#want to store in string instead of list
password_str = ""
for char in password_list:
    password_str += char
print(password_str)
