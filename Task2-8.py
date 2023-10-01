import turtle as t

t.shape('turtle')
x = 5
y = 10
n = 100
for i in range(n):
    for k in range(2):
        t.forward(x)
        t.right(90)
    x += y