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

textViewer = turtle.Turtle()
textViewer.hideturtle()
textViewer.penup()
textViewer.goto(0,0)

def drawClock(clockviewer,radius):
    clockviewer.clear()
    clockviewer.penup()
    clockviewer.goto(0,-radius)
    clockviewer.pendown()
    clockviewer.circle(radius)
    
    for i in range(12):
        clockviewer.penup()
        clockviewer.goto(0,0)
        clockviewer.setheading(90-i*30)
        clockviewer.forward(radius-10)
        clockviewer.pendown()
        clockviewer.forward(20)
        clockviewer.penup()
        clockviewer.goto(0,0)
        clockviewer.forward(radius-40)
        clockviewer.write(i+1, align='center', font=('Courier', 12, 'normal'))

def timeViewer(clockViewer, angle, color, length=180):
    clockViewer.penup()
    clockViewer.home()
    clockViewer.color(color)
    clockViewer.pendown()
    clockViewer.setheading(90-angle)
    clockViewer.forward(length)

drawClock(clockViewer,200)

while True:
    viewer.clear()
    now = datetime.now()
    
    hour = now.hour % 12
    minutes = now.minute
    second = now.second
    micro = now.microsecond

    textViewer.clear()
    textViewer.write(f'{hour:02d}:{minutes:02d}:{second:02d}', align='center', font=('Courier', 24, 'normal'))
    
    # Smidiga vinklar
    hour_angle = 30*hour + 0.5*minutes + (0.5/60)*(second + micro/1_000_000)
    minute_angle = 6*minutes + 0.1*second + 0.0001*micro
    second_angle = 6*second + 0.000006*micro

    timeViewer(viewer, hour_angle, 'blue', 100)
    timeViewer(viewer, minute_angle, 'green', 150)
    timeViewer(viewer, second_angle, 'red', 180)
    
    screen.update()
    time.sleep(0.05)