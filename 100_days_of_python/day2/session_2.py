print("welcome to the roller coaster")
height = int(input("enter your height "))
bill = 0
if height > 120:
    print("you can ride the roller coaster")
    age = int(input("enter your age "))
    if age <= 12:
        bill += 5
        print("child ticket pay $5")
    elif age <= 18:
        bill += 7
        print("youth ticket pay $7")
    else:
        bill += 12
        print("adult ticket pay $12")
    want_photo = input("enter are you want photo yes or no: ")
    if want_photo == "yes":
        bill += 3
    print(f"your final bill is: ${bill}")
else:
    print("you can't ride the roller coaster")