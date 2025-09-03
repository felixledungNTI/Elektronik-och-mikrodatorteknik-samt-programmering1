import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for i in range(12):
    t.penup()
    t.setheading(i * 30)
    t.forward(60)
    t.right(90)
    t.pendown()
    t.color('yellow')
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()
    
    t.penup()
    t.right(90)
    t.forward(10)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
    t.penup()
    t.right(90)
    t.backward(70)
    t.setheading(0)
    
turtle.done()