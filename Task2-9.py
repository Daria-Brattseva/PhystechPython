import turtle

turtle.shape('turtle')
n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i, j in zip(n, d):
    turtle.circle(j,360,i)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()