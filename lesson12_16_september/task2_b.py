import turtle
import time

s = turtle.getscreen()
s.bgcolor('black')
t = turtle.Turtle()

radius = 25

t.shape('square')
t.color('green')

t.circle(radius)

while True:
    t.shape('square')
    time.sleep(0.3)
    t.shape('turtle')
    time.sleep(0.3)

turtle.done()