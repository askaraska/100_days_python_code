# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) # <_csv.reader object at 0x0000022A9F627CA0>
#     temperatures = []
#     for row in data:
#         # print(row) # ['day', 'temp', 'condition'] .. like other all data
#         # print(row[1]) # temp 12 14 15 14 21 22 24
#         if row[1] != "temp":
#             # temperatures.append(row[1]) # ['12', '14', '15', '14', '21', '22', '24']
#             temperatures.append(int(row[1])) # [12, 14, 15, 14, 21, 22, 24]
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

#         day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny

print(data["temp"])

# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24
# Name: temp, dtype: int64

data_dict = data.to_dict()
print(data_dict)
#o/p
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
# 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
# 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

temp_list = data["temp"].to_list()
print(temp_list) # [12, 14, 15, 14, 21, 22, 24]
print(len(temp_list)) # 7

#finding average temperature

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp) # 17.428571428571427

print(data["temp"].mean()) # 17.428571428571427 shortcut

#finding maximum temperature
print(data["temp"].max()) # 24

#get data in columns
print(data["condition"])
print(data.condition)

#o/p:
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object

# get data in rows

print(data[data.day == "Monday"])

#o/p
#       day  temp condition
# 0  Monday    12     Sunny

#picking highest temp in row
print(data[data.temp == data.temp.max()])

#      day  temp condition
# 6  Sunday    24     Sunny

monday = data[data.day == "Monday"]
print(monday.condition)
# 0    Sunny
# Name: condition, dtype: object

#create dataframe from scratch
datas_dict = {
    "students" : ["Amy","James","Askar"],
    "scores" : [76,56,65]
}
frame = pandas.DataFrame(datas_dict)
print(frame)

#   students  scores
# 0      Amy      76
# 1    James      56
# 2    Askar      65

frame.to_csv("students_data.csv")