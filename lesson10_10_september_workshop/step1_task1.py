import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

t.pensize(2.5)
t.pencolor('black')

radius1 = 150
radius2 = 95
radius3 = 40
radiusVerySmall = 5

t.penup()
t.begin_fill()
t.goto(0,-350)
t.pendown()
t.circle(radius1)
t.color('blue')
t.end_fill()

t.penup()
t.begin_fill()
t.goto(0, -75)
t.pendown()
t.circle(radius2)
t.color('blue')
t.end_fill()

t.penup()
t.begin_fill()
t.goto(0,105)
t.pendown()
t.circle(radius3)
t.color('red')
t.end_fill()

t.setheading(180)
t.penup()
t.begin_fill()
t.goto(0, 210)
t.color('#2e2e2e')
t.pendown()
t.forward(100)
t.right(90)
t.forward(25)
t.left(90)

t.forward(100)
t.left(90)
t.forward(25)
t.right(90)

t.forward(100)
t.left(90)
t.forward(25)
t.right(90)

t.backward(300)
t.left(90)
t.forward(25)

t.penup()
t.begin_fill()
t.goto(0,130)
t.pendown()
t.circle(radiusVerySmall)
t.color('orange')
t.end_fill()

t.penup()
t.begin_fill()
t.goto(-25,150)
t.pendown()
t.circle(radiusVerySmall)
t.color('white')
t.end_fill()

t.penup()
t.begin_fill()
t.goto(25,150)
t.pendown()
t.circle(radiusVerySmall)
t.color('white')
t.end_fill()

t.pensize(5)
t.pencolor('black')

t.penup()
t.begin_fill()
t.goto(0,25)
t.pendown()
t.circle(radiusVerySmall)
t.color('white')
t.end_fill()

t.pensize(5)
t.pencolor('black')

t.penup()
t.begin_fill()
t.goto(0,50)
t.pendown()
t.circle(radiusVerySmall)
t.color('white')
t.end_fill()

t.pensize(5)
t.pencolor('black')

t.penup()
t.begin_fill()
t.goto(0,75)
t.pendown()
t.circle(radiusVerySmall)
t.color('white')
t.end_fill()

t.hideturtle()

turtle.done()