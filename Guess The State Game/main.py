#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temp = []
#    for row in data:
#        if row[1] != "temp":
#            temp.append(int(row[1]))
#    print(temp)
import pandas
data = pandas.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#print(data.to_dict())
#temp_list = data["temp"].to_list() # when we use data["temp"] we get series of temp and we can convert a series into list in pandas
#avg of temp:
#print(data["temp"].mean())
#print(data["temp"].mode())
#print(data["temp"].max())
#print(temp_list)

#get data in columns
#print(data["condition"])
#or
#print(data.condition)

#get data in row
#print(data[data.day == "Monday"])
#print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#create a dataframe from scratch
dict = {
    "students": ["amy", "scot"],
    "scores": [1, 2]
}
data = pandas.DataFrame(dict)
data.to_csv("new_data.csv")