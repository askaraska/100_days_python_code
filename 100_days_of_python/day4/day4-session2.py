# understanding offset and python lists
country = ["india","australia","pakistan","SA","NZ","england"]
print(country)
print(country[0])
print(country[1])
print(country[-1])
# ===============================================================

# change value in lists:
country[3] = "south africa"
print(country)

# add items in lists:
country.append("afghanistan")
print(country)

country.extend(["west indies","netherland"])
print(country)
# =================================================================== #

# task1 : pick random name list of friends

friends = ["haji","askar","ammar","sheikh"]
print(friends)
# method 1: have inbuilt function random.choice()
import random
print(random.choice(friends))

# method 2: random.randint() (0,1,2,3) stored in random_index
random_index = random.randint(0,4)
print(friends[random_index])  #  friends[0],friends[1]..friends[3]

# =====================================================================

# out of range error in list
# l1 = ["apple","banana","orange"]
# print(l1[3])
# =====================================================================

print(len(friends)) # length of friends list

fruits = ["apple","orange","banana"]
vegetables = ["brinjal","spinach"]
dirty_frozen = [fruits,vegetables] # two lists in one.
print(dirty_frozen)

