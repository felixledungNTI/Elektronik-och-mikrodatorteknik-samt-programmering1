import turtle
import time

tr = turtle.Turtle()
wn = turtle.Screen()

tr.hideturtle()

wn.setup(width=500,height=500)
wn.bgpic('lesson25_13_october/linearGradient.gif')
wn.update()
time.sleep(1)
wn.bgpic('lesson25_13_october/pythonLogo.gif')

turtle.done()