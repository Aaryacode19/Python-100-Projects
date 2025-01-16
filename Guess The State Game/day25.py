import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count)

data_dict = {
    "Fur color": ['Gray', "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirel_count.csv")