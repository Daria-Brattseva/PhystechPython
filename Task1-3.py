import matplotlib.pyplot as plt
import numpy as np

def function (x : int) -> int:
    y = np.log((x*x+1)*np.exp(np.abs(x)/-10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x))))
    return y

x = [-100, -50, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100]
y = []
for i in range (len(x)):
    y.append(function(x[i]))
plt.plot(x,y)
plt.grid(True)
plt.show()

