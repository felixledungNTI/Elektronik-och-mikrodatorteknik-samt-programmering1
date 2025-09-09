import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.color('blue')

def vimpel():
    t.forward(100)
    t.right(100)
    t.forward(40)
    t.right(160)
    t.forward(40)
    t.right(100)

t.setheading(90)
vimpel()

turtle.done()