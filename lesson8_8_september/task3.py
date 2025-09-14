import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for c in range(16):
    t.forward(10+5*c)
    t.left(90)
    
turtle.done()