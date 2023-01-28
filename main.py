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

import pandas as pd

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

fish = {"Salmon", "Tuna", "Mackerel", "Anchovy", "Sardine"}
fish.discard("Tuna")
print(fish)
