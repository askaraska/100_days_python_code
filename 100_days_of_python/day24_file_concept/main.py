# file = open("my_file.txt") # opened the file
# print(file)

# contents = file.read()
# print(contents)
# --------------------------------------------------
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# "Hello, My Name is Askar"
# i'm 28 years old
# -----------------------------------------------

# with open("my_file.txt") as file: # open file as the read mode so can't write
#     file.write("new text")

# with open("my_file.txt", "w") as file:
#     file.write("edited and old one goes")
#
# with open("my_file.txt", "a") as file:
#     file.write("\nwith existed one add new one")
# file.close()
#
# #new file created
# with open("new_file.txt", "w") as file:
#     file.write("new file created on folder")
# with open("/Users/SULTHAN ASKAR/Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # moving file to another directory and access from that using absolute file path

# with open("../../../../Desktop/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# using relative