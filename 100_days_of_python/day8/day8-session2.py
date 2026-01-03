#psitional vs keyword argument
#function with more than one input
#positional argument program ex:
def greet_with(name,location):
    print(f"hello {name}")
    print(f"location is {location}")
greet_with("askar","klk")
greet_with("klk","askar")
#=======================================

#keyword argu:
def greet_with_key(name,location):
    print(f"hello {name}")
    print(f"location is {location}")
greet_with_key(name="angela",location="london")
greet_with_key(location="london",name="angela")
#=============================================
