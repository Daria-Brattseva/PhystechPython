import matplotlib.pyplot as plt
import numpy as np

def function (x : int) -> int:
    y = x*x-x-6
    return y

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
for i in range (len(x)):
    y.append(function(x[i]))
plt.plot(x,y)
plt.grid(True)
plt.show()