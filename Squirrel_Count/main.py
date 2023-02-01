

import pandas

data = pandas.read_csv("Squirrel_Count/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(f"Gray squirrels: {grey_squirrels_count}\nRed squirrels: {cinnamon_squirrels_count}\n"
      f"Black squirrels: {black_squirrels_count}")

data_dict = {
      "Fur Color": ["Gray", "Red", "Black"],
      "Quantity": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Color_Counts.csv")

# fur_colors = data["Primary Fur Color"].value_counts()
# print(fur_colors)
