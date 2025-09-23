import turtle
import time
from datetime import datetime

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

viewer = turtle.Turtle()
viewer.hideturtle()
viewer.speed(0)

clockViewer = turtle.Turtle()
clockViewer.speed(0)
clockViewer.pensize(3)

#draw clock circle

def drawClock(clockviewer,radius):
    clockviewer.penup()
    clockviewer.goto(0,-radius)
    clockviewer.pendown()
    clockviewer.circle(radius)

#make some time viewer

def timeViewer(clockViewer, angle):
    clockViewer.penup()
    clockViewer.goto(0,0)
    clockViewer.pendown()
    clockViewer.forward(315)
    clockViewer.right(angle)
    
    return timeViewer

drawClock(clockViewer,365)

def currentTime():
    hour = datetime.hour
    minutes = datetime.minute
    second = datetime.second
    
    return hour, minutes, second

#Display current time

turtle.write(currentTime(), align='center', font=('Courier',24,'normal'))

while True:
    timeViewer(clockViewer, 10)
    screen.update()
    time.sleep(1)
    
    clockViewer.penup()
    clockViewer.home()
    drawClock(clockViewer,365)
    clockViewer.pendown()
    
    
screen.update()

turtle.done()