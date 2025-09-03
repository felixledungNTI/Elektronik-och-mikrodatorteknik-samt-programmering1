import turtle

s = turtle.getscreen()
t = turtle.Turtle()

radius = 50
width = 15

t.pensize(width)
t.color("black", "blue") 


t.penup()
t.begin_fill()
t.goto(0,-radius)
t.pendown()
t.circle(radius)
t.end_fill()

t.penup()
t.begin_fill()
t.goto(190,-radius)
t.pendown()
t.circle(radius)
t.end_fill()

t.penup()
t.begin_fill()
t.goto(380,-radius)
t.pendown()
t.circle(radius)
t.end_fill()

turtle.done()