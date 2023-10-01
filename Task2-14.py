import turtle as t

t. shape('turtle')

for i in range(5):
    t.left(180 - (180 / 5))
    t.forward(200)
t.penup()
t.goto(200, 0)
t.pendown()
for i in range(11):
    t.left(180 - (180 / 11))
    t.forward(200)