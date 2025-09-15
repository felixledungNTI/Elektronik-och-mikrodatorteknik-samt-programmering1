import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.penup()
t.color('green')
t.shape('circle')

while True:
    t.sety(t.ycor()-1)
    
turtle.done()