

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = data["Primary Fur Color"].value_counts()
print(fur_colors)

