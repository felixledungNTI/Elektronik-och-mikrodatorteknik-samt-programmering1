import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(10)

t.pensize(2.5)

radius1 = 150
radius2 = 95
radius3 = 40
radiusVerySmall = 5

t.penup()
t.pencolor('black')
t.begin_fill()
t.goto(0,-350)
t.pendown()
t.circle(radius1)
t.color('blue')
t.end_fill()

t.penup()
t.pencolor('black')
t.begin_fill()
t.goto(0, -75)
t.pendown()
t.circle(radius2)
t.color('blue')
t.end_fill()

t.penup()
t.begin_fill()
t.pencolor('black')
t.goto(0,105)
t.pendown()
t.circle(radius3)
t.color('red')
t.end_fill()

t.setheading(180)
t.penup()
t.pencolor('#2e2e2e')
t.begin_fill()
t.goto(150, 210)
t.fillcolor('#2e2e2e')
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

# Important
t.backward(300)
t.right(90)
t.forward(25)
t.end_fill()

t.penup()
t.begin_fill()
t.pencolor('orange')
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
t.goto(25,150)
t.pendown()
t.pencolor('orange')
t.fillcolor('white')
t.begin_fill()
t.circle(radiusVerySmall)
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