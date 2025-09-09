import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.shape('turtle')

def rectangle():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)
    t.right(90)
    t.backward(100)
    t.left(90)

for c in range(4):
    rectangle()
    
turtle.done()