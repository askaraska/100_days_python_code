"""Inheritance in Python is a core principle of object-oriented programming (OOP)
 that allows a new class (child or derived class)
  to inherit attributes and methods from an existing class (parent or base class)."""
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breath(self):
        print("inhale, exhale")


class Fish(Animal): #  Fish class inherit things from animal class
    def __init__(self):
        super().__init__() # keyword

    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("swim, moving in the water")

nemo = Fish()
nemo.swim()
nemo.breath()
print(nemo.num_eyes)