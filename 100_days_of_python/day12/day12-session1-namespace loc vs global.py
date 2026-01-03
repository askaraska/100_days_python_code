"""NAMESPACES: local vs global scope"""
#scope: apple treee example
# starting of

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside the function: {enemies}") # o/p: 2

increase_enemies()
print(f"enemies outside the function", enemies) # o/p: 1

# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength) #o/p:2
#
# drink_potion()
# print(potion_strength) # o/p: NameError: name 'potion_strength' is not defined, ulla define panna var can't use at outside
#==========================================================================================================================#
# global scope
player_health = 10

def player_drink():
    water = "black water"
    print(player_health)  # o/p:10

player_drink()
#==================================================#


