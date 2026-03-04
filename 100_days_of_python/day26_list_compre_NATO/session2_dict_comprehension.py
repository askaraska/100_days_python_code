# new_dict = {new_key:new_value for item in list} - dict_list_comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items()} take existing dict
# new_dict = {new_key:new_value for (key,value) in dict.items() if tests}


"""looping through the list"""
names = ["Bob", "Alice", "Carol", "David","haji"]
import random
# new_dict = {new_key:new_value for item in list}
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
# {'Bob': 34, 'Alice': 67, 'Carol': 60, 'David': 89, 'haji': 39}

"""looping through the dictionary"""
passed_students = {student:score for (student, score) in students_scores.items() if score >= 35}
print(passed_students)
# {'Alice': 67, 'Carol': 60, 'David': 89, 'haji': 39}
