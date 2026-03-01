import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#once successfully read that csv,now got a data frame
#get gray primary fur color
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrels)

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
