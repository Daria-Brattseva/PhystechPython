import numpy as np

x = [1, 10, 100]
n = 3
for i in range (n):
    y = np.log((np.e)**(1/np.sin(x[i])+1)/(5/4+1/x[i]**15))/np.log(1+x[i]*x[i])

for i in x:
    y = np.log((np.e)**(1/np.sin(i)+1)/(5/4+1/i**15))/np.log(1+i*i)
    print(y)