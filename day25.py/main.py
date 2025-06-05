# with open("100DOC/day25.py/weather_data.csv", "r") as data_file:
#     data = data_file.readlines()

# print(data)

# import csv

# with open("100DOC/day25.py/weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)
    

import pandas

data = pandas.read_csv("100DOC/day25.py/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)
# print(data["temp"][0])

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data_dict)
# sum_temp = 0
# # for i in temp_list:
# #     sum_temp += i

# # avg_temp = sum_temp/len(temp_list)
# # print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

#get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_f = monday.temp * (9/5) + 32
# print(monday_f)

# #Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# print(data[data.students == "Amy"])

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

count_dict: dict = {
    "Fur Color":  ["grey", "red", "black"],
    "Count":  [gray_count, cinnamon_count, black_count]
    }

squirrel_count = pandas.DataFrame(count_dict)
squirrel_count.to_csv("100DOC/day25.py/squirrel_count.csv")