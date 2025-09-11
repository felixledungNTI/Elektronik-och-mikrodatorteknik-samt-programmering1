import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

t.pensize(2.5)

radius1 = 150
radius2 = 95
radius3 = 40
radiusVerySmall = 5

t.penup()
t.pencolor('black')
t.begin_fill()
t.fillcolor('white')
t.goto(0, -350)
t.pendown()
t.circle(radius1)
t.end_fill()

t.penup()
t.pencolor('black')
t.begin_fill()
t.fillcolor('white')
t.goto(0, -75)
t.pendown()
t.circle(radius2)
t.end_fill()

t.penup()
t.begin_fill()
t.pencolor('black')
t.goto(0, 105)
t.pendown()
t.circle(radius3)
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

#mun

t.setheading(180)
t.penup()
t.goto(15, 130)
t.pendown()
t.forward(25)

t.penup()
t.goto(-20, 155)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(30, 155)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(5)
t.end_fill()

#arm1
t.setheading(25)
t.penup()
t.goto(95, 0)
t.pendown()
t.forward(45)

t.setheading(65)
t.penup()
t.goto(135, 20)
t.pendown()
t.forward(10)

t.setheading(-65)
t.penup()
t.goto(135, 20)
t.pendown()
t.forward(10)

#arm2
t.setheading(155)
t.penup()
t.goto(-95, 0)
t.pendown()
t.forward(45)

t.setheading(115)
t.penup()
t.goto(-135, 20)
t.pendown()
t.forward(25)

t.setheading(115)
t.penup()
t.goto(-135)

t.hideturtle()

turtle.done()
t.penup()
t.goto(-135, 20)
t.pendown()
t.forward(10)