# with open("data.csv") as data :
#     data = data.readlines()
#     print(data)

import csv

with open("data.csv") as data_file :
    data = csv.reader(data_file)
    temp = []
    for row in data :
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)

import pandas as pd
data = pd.read_csv("data.csv")
print(data["temp"])