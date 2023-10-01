import turtle as t
import numpy as np

t.shape('turtle')

x = 0
for i in range(10000):
    t.forward(x/2*np.pi)
    t.left(2*np.pi)
    x += 0.01