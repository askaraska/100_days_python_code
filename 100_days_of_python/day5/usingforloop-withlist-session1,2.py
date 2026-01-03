fruits = ['apple', 'banana', 'orange', 'strawberry']
for fruit in fruits:
    print(fruit) #strawberry
    print(fruit+" pie") #strawberry pie
    print(fruits)

#haveibeenpwned.com loop workflow

#caluclate the total sum using sum()
student_scores = [70, 80, 90, 100]
total_student_score = sum(student_scores)
print(total_student_score)
# using loop

student_scores_l1 = [70, 80, 90, 100]
sum = 0
for score in student_scores_l1:
    sum += score
    print(sum) #each one add and print result
print(sum) # proper total final single result 340

#find largest in list - using max():
larger_score = max(student_scores)
print(larger_score) # 100

##find largest in list - using for loop:
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score) #100


