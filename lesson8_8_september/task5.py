import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.color('blue')

def vimpel(x,y, angle):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()
    
    t.forward(100)
    t.right(100)
    t.forward(40)
    t.right(160)
    t.forward(40)
    t.right(100)

x = 0
y = 0

t.setheading(90)
vimpel(0,0,0)
vimpel(-50, 25, 25)
vimpel(-100,50, 95)

turtle.done()