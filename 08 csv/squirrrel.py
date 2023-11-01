import pandas as pd

data = pd.read_csv("tupai.csv")
# data = pd.read_csv("data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Red", "Black"],
    "Count"     : [gray_squirrels, red_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv("squirrel_csv")