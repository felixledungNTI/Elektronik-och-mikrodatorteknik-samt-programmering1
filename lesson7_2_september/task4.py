import turtle

s = turtle.getscreen()
t = turtle.Turtle()

length = 600
height = 280
color1 = 'blue'

t.color(color1)
t.begin_fill()

t.forward(length)
t.right(90)
t.forward(height)
t.right(90)
t.forward(length)
t.right(90)
t.forward(height)
t.end_fill()

turtle.done()