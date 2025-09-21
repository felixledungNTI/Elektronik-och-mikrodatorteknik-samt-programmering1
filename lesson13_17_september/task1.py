import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

radius = 35

turtle.bgcolor('black')

t.pencolor('white')
for a in range(2):
    t.forward(150)
    t.left(90)
    t.forward(275)
    t.left(90)
    
pos = [(75,50),(75,130),(75,210)]

t.color('gray')

def drawLightCircle(pos,color):
    t.penup()
    t.goto(pos[0],pos[1]-radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def resetLight():
    for i in pos:
        drawLightCircle(i,'gray')

def trafficLight():    
    resetLight()
    drawLightCircle(pos[0], 'red')
    time.sleep(1)
    
    resetLight()
    drawLightCircle(pos[0],'red')
    drawLightCircle(pos[1], 'yellow')
    time.sleep(1)
    
    resetLight()
    drawLightCircle(pos[2],'green')
    time.sleep(1)
     
    resetLight()
    drawLightCircle(pos[1], 'yellow')
    time.sleep(0.5)

while True:
    trafficLight()

turtle.done()