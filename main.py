import csv

# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for i in data:
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list)/len(temp_list)
# print(average)

# max_val = data["temp"].max()
# print(max_val)

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])

# max_val = data["temp"].max()
# a = (data.temp)
# print(type(a))

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data[data["Primary Fur Color"] == "Gray"])