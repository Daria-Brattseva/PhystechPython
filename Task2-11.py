import turtle as t

t.shape('turtle')
t.left(90)
n = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(n)):
    for k in range(int(360/n[i])):
        t.forward(1)
        t.left(n[i])
    for k in range(int(360/n[i])):
        t.forward(1)
        t.right(n[i])

