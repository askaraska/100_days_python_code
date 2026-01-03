import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

# easy level = dLPN#(25
print("welcome to python password generator")
nos_letters = int(input("how many letters would you like in password ? :\n")) #if i enter 4 means,
# 4 stored in nos_letters
nos_symbols = int(input(f"how many symbols would you like in password ? :\n"))
nos_numbers = int(input("how many numbers would you like in password ? :\n"))
password = ""               # password string empty
for char in range(0,nos_letters): # range: 0,1,2,3 = 4 enter via for loop
    password += random.choice(letters) # 4 iteration happens and randomly choose 4 letters from letters list
for char in range(0,nos_symbols): # range: 0,1,2,3 = 4 enter via for loop
    password += random.choice(symbols)  # 4 iteration happens and randomly choose 4 symbols from symbols list
for char in range(0,nos_numbers): # range: 0,1,2,3 = 4 enter via for loop
    password += random.choice(numbers) # 4 iteration happens and randomly choose 4 numbers from numbers list
print(password)
"""this give such format letter,symbol,number"""