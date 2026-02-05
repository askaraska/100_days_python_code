class Car:
    def __init__(self):
        print("Car obj being Created") # when object created it will be 1st executed from init function

car1 = Car() # object created
car1.name = "Toyota"
car1.model = 2026
print(car1.name)

car2 = Car() # o/p: New car being Created - due to init function (constructor)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User("Askar",28)
print(user1.name)
print(user1.age)


user2 = User("sumayya",24)
# user2.name = "askar"
# user2.age = 24
print(user2.name)
print(user2.age)

