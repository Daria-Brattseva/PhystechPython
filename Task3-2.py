import turtle


#for 0
def zero():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)

#for 1
def one():
    turtle.shape('turtle')
    turtle.left(45)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

#for 2
def two():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(71)
    turtle.left(135)
    turtle.forward(50)
    turtle.penup()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)

#for 3
def three():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(71)
    turtle.left(135)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(71)
    turtle.penup()
    turtle.left(45)

#for 4
def four():
    turtle.shape('turtle')
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)

#for 5
def five():
    turtle.shape('turtle')
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)

#for 6
def six():
    turtle.shape('turtle')
    turtle.right(135)
    turtle.forward(71)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)

#for 7
def seven():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(71)
    turtle.left(45)
    turtle.forward(50)

#for 8
def eight():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)

#for 9
def nine():
    turtle.shape('turtle')
    turtle.left(45)
    turtle.forward(71)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.right(135)
    turtle.forward(71)
    turtle.left(45)

numbers = input()
for i in numbers:
    # print(i)
    if i == '0':
        zero()
    elif i =='1':
        one()
    elif i =='2':
        two()
    elif i =='3':
        three()
    elif i =='4':
        four()
    elif i =='5':
        five()
    elif i =='6':
        six()
    elif i =='7':
        seven()
    elif i =='8':
        eight()
    elif i =='9':
        nine()
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
