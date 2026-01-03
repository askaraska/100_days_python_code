print("welcome to python pizza deliveries")
size = input("enter your size of pizza ? s,m,l: ")
pepperoni = input("do you want pepperoni ? yes or no:")
extra_cheese = input("do you want extra cheese ? yes or no:")
bill = 0
# todo: how much they need to pay based on size of their pizzas
if size == "s":
    bill = bill + 15
elif size == "m":
    bill = bill + 20
elif size == "l":
    bill = bill + 25
else:
    print("wrong input")
#     how much add to their bill for pepperoni
if pepperoni == "yes":
    if size == "s":
        bill = bill + 2
    else:
        bill = bill + 3
# how much add to their bill for extra_cheese
if extra_cheese == "yes":
    bill = bill + 1
print(f"your final bill is: ${bill}")