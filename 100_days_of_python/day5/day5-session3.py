#===========================for loop and the range() function=======================#:

for num in range(1, 11): #takes 1 to 10 range
    print(num)

#step by:
for num in range(1, 11, 2):
    print("step by")
    print(num)

# want to add 1 to 100 using for loop and range ():
res = 0
for i in range(1,101):
    res = res + i
    print(res)  #output with adding each iteration
print(res)    #o/p: 5050