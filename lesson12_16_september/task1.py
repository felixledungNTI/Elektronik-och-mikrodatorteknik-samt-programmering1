import turtle
import time

s = turtle.getscreen()
s.tracer(0)
t = turtle.Turtle()
t.hideturtle()

radius = 25
xAngle = -200
yAngle = 0

for c in range(100):
    t.clear()
    t.penup()
    t.goto(xAngle,yAngle-radius)
    t.pendown()
    t.begin_fill()
    t.color('green')
    t.circle(radius)
    t.end_fill()
    
    xAngle += 10
    s.update()
    time.sleep(0.5)

turtle.done()