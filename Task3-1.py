import turtle

from random import *

turtle.shape('turtle')
for i in range(100):
    turtle.forward(randint(1, 10))
    turtle.left(randint(0, 360))
