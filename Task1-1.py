import numpy as np

x=int(input())
y=np.log((np.e)**(1/np.sin(x)+1)/(5/4+1/x**15))/np.log(1+x*x)
print (y)