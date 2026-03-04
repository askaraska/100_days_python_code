student_dict = {
    "student": ["Askar","Sumayya","Ammar"],
    "score": [56,76,98]
}

# looping through dictionary:
for (key,value) in student_dict.items():
    # print(key) # student score
    print(value) #['Askar', 'Sumayya', 'Ammar'] [56, 76, 98]

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#    student  score
# 0    Askar     56
# 1  Sumayya     76
# 2    Ammar     98

# looping through a data frame

# for (key,value) in student_data_frame.items():
#     print(key) # student score
#     # print(value)

#pamdas inbuilt loop
#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index) # 0 1 2
    print(row)
    # print(row.student) # Askar Sumayya Ammar
    print(row.score)