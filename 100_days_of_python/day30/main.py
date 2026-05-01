#FileNotFoundError:
# with open("a_file.tx") as file:
#     file.read()

# #keyError
# my_dict = {"key1":"value1"}
# value = my_dict["non_existent_key"]

#IndexError: list index out of range
# fruit_list = ["apple", "banana", "cherry"]
# fruit = fruit_list[3]

#TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt","w")
#     file.write("open file if there is exists, else create new file")

#     print(a_dictionary["keynotexist"])
# KeyError: 'keynotexist'

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("open file if there is exists, else create new file")
# except KeyError as error_message:
#     print(f"key {error_message} not exists")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file closed")
#     raise TypeError("this is the error that i made up")


height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("human height should not be over 3 metres.")
bmi = weight / (height ** 2)
print("bmi is", bmi)