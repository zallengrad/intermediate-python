import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

df = pd.read_csv("dataiwakku.csv")
reg = LinearRegression()
reg.fit(df[['x1', 'x2']].values, df.y)

mpl.rcParams['legend.fontsize'] = 12
fig = plt.figure()
ax = fig.add_subplot(projecttion = '3d')
ax.scatter(df.x1, df.x2, df.y)
ax.legend()
ax.view_init(45,0)
plt.show()