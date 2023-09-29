import turtle as t

t.shape('turtle')
for i in range(3):
    for i in range(180):
        t.forward(1)
        t.left(2)
    for i in range(180):
        t.forward(1)
        t.right(2)
    t.left(60)