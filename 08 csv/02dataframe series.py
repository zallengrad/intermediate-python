import pandas as pd

data = pd.read_csv("data.csv")
data_dic = data.to_dict()
data_list = data["temp"].to_list()
rata_rata = sum(data_list) / len(data_list)
mean = data["temp"].mean()
max = data["temp"].max()
# max = data.temp.max() --- beda penulisan sama saja


# print(data_dic)
# print(data_list)
# print(rata_rata)
# print(mean)
# print(max)

#
# print(data[data.day == "senin"])
# print(data[data.temp == max ])

# get data in row
senin = data[data.day == "senin"]
# print(senin.temp)
celc = senin.temp
farenheit = (celc * 9/5) + 32
print(farenheit)

# create a dataframes from scratch
data_dict = {
    "students"  : ["zale", "james", "akil"],
    "score"     : [100, 80, 32]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new data.csv")