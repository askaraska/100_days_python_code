# List Comprehension
# List comprehension offers a shorter syntax
# when you want to create a new list
# based on the values of an existing list.
#new_list = [new_item for item in list] --- formula
#new_list = [new_item for item in list if test] --- with cond in list

#for loop

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# o/p: ['apple', 'banana', 'mango']
# ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]

print(new_list)

numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers) #[2, 3, 4]

name = "Askar"
latter_list = [letter for letter in name]
print(latter_list) # ['A', 's', 'k', 'a', 'r']

range_list = [x * 2 for x in range(1,5)]
print(range_list)  # [2, 4, 6, 8]

names = ["haji","farhan","fahad","askar","ammar"]
short_names = [name for name in names if len(name)<5]
print(short_names) #['haji']
# need > 5 with capital letter
long_names = [l_name.upper() for l_name in names if len(l_name)>5]
print(long_names) #['FARHAN']
