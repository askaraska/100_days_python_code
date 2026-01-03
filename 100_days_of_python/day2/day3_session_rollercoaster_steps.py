water_level = 85
if water_level > 80:
    print("drain water")
else:
    print("continue water level")

# > , <, >= , <= , == , !=
#     == check equality
# number check for even or odd
# roller coaster problem based on height 1st check
print("welcome to roller coaster")
height = int(input("enter your height "))
if height > 120:
    print("you can ride the roller coaster")
else:
    print("you can't ride the roller coaster")

# after we have to check age: age = 18 or more allowed, else not allowed
print("welcome to roller coaster")
height = int(input("enter your height "))
if height > 120:
    print("you can ride the roller coaster")
    age = int(input("enter your age "))
    if age >= 18:
        print("you can ride the roller coaster")
else:
    print("you can't ride the roller coaster")

# after we have set bill based on age:age >= 18 = 12$ , age: age < 18  =7$
print("welcome to roller coaster")
height = int(input("enter your height "))
if height > 120:
    print("you can ride the roller coaster")
    age = int(input("enter your age "))
    if age <= 18:
        print("you pay 7$")
    else:
        print("pay 12$")
else:
    print("you can't ride the roller coaster")