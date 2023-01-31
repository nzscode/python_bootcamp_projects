# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
import pandas
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
data_list = data["temp"].to_list()
max = data["temp"].max()
print(max)