# def add(*args):
#     for n in args:
#         print(n)
#
# add(2,3,4)

# o/p:
# 2
# 3
# 4

def add(*args):
    """unlimited positional arguments"""
    print(args[0]) # o/p: 2
    sum = 0
    for num in args:
       sum += num
    return sum

print(add(2,3,4,5,6)) # o/p: 20
# =================================================
def calculate(n, **kwargs):
    print(kwargs) # {'add': 3, 'multiply': 5} stores like dict
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"] # n=2, kwargs["add"] = 3 --> so, 2 += 3 equal to 5
    n *= kwargs["multiply"] # now n=5, kwargs["multiply"] = 5 so, 5 *= 5 = 25
    print(n) # 25


calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)