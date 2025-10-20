import turtle

s = turtle.Screen()
t = turtle.Turtle()

#stam
t.penup()
t.goto(0,0)
t.pendown()
t.right(90)
t.backward(100)

def treePin(x,y, rotate,len):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(rotate)
    t.forward(len)

treePin(0,100, 130,100)
treePin(-75,160,-40,50)

treePin(-125,160,-40,50)
treePin(-125,160,80,50)

treePin(-75,160,30,50)
treePin(-90,200,60,50)
treePin(-90,200,-60,50)

treePin(0,100,-130,100)
treePin(75,160,40,50)

#mirror

turtle.done()