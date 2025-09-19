import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.penup()
color = 'red'
t.color(color)
t.shape('circle')

while True:
    t.sety(t.ycor()-1)
    
    if color == 'red':
        color = 'green'
    else:
        color = 'red'
        
    t.color(color)
    
    time.sleep(0.2)
    
turtle.done()