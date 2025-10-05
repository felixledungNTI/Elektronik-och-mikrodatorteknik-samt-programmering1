import turtle

s = turtle.Screen()
s.setup(500,500)
s.tracer(0)
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.hideturtle()

def square():
    for s in range(4):
        t.forward(100)
        t.left(90)
        
t.penup()
t.goto(-350,0)
t.pendown()

while True:
    t.clear()
    square()
    s.update()
    t.forward(0.2)