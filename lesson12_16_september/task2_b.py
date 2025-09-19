import turtle
import time

s = turtle.getscreen()
s.bgcolor('black')
s.tracer(0)
t = turtle.Turtle()

radius = 25

def circle(color):
    t.penup()
    t.goto(0,-radius)
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()
    
def square(color):
    t.penup()
    t.goto(150,0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for c in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()

while True:
    circle('green')
    square('green')
    s.update()
    time.sleep(0.5)
    
    t.clear()
    s.update()
    time.sleep(0.5)
    
turtle.done()