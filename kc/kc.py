import matplotlib.pyplot as plt
from scipy import stats


#x= [10,28,29,35,48,55,71,73,80,88,91,111,131,144,168]
#y = [29,47,55,65,79,82,92,95,100,102,110,124,127,130,152]
x = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
y = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]

slope, intercept, r, p, std_err = stats.linregress (x, y)

print('slope', slope)
print('intercept', intercept)

slope = 0.10976773783009863
intercept = 98.24832962138083

def myfunc (x):
    return intercept + slope * x

mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

print(f"harga rumah jika luasan = 2500 yaitu sebesar {myfunc(2500)}")
