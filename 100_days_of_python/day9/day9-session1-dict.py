# #================================ THE PYTHON DICTIONARY=============================#
# #Dictionary syntax: {key:value}
#
# 1. Basics of Dictionaries:
# Definition: A dictionary in Python is an unordered collection of items. Each item is a key-value pair.
# Syntax: {key1: value1, key2: value2, ...}
#===========================================================#
# creating dict and more than one key value pair:
programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"The piece of code that you can easily call over again",
}
#retrieve all data from dictionary
print(programming_dictionary)
# retrieve item from dictionaries
print(programming_dictionary["Function"])

# #error:
# programming_dictionary_error = {
#     "Bug":"An error in a program.",
#     "Function":"can easily call over again",
#     123: "something"
# }
# print(programming_dictionary_error["Bog"]) #key error
# print(programming_dictionary_error[123]) # print something

# adding new entry in dictionary:
programming_dictionary["Loop"] = "something call over again and again."
print(programming_dictionary)

#creating empty dictionary : empty_dictionary = {}

#dummy dictionary created for wipe out process:
dummy_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"The piece of code that you can easily call over again",
}
print(dummy_dictionary)
#wipe an existing dictionary:
dummy_dictionary = {}
print(dummy_dictionary)

# edit an item in dictionary:
programming_dictionary["Function"] = "reusable code."
print(programming_dictionary)

# Looping through dictionary:
for thing in programming_dictionary:
    print(thing) # only retreive  keys: Bug Function Loop

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # it give expected result proper iteration.

