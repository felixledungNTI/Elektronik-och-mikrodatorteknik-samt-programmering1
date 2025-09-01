import turtle

s = turtle.getscreen()
t = turtle.Turtle()

#make half circle



t.penup() 
t.goto(-150,0)
t.pendown()
t.color("cyan")
t.setheading(90)
t.width(10)
t.circle(100, 180)

t.penup()
t.goto(100,0)
t.pendown()
t.color("black")
t.setheading(90)
t.width(10)
t.circle(100, 180)

t.penup()
t.goto(350,0)
t.pendown()
t.color("red")
t.setheading(90)
t.width(10)
t.circle(100,180)

t.penup()
t.goto(-25, -115)
t.pendown()
t.color("yellow")
t.setheading(270)
t.width(10)
t.circle(100,180)

t.penup()
t.goto(-225, -115)
t.pendown()
t.color("green")
t.setheading(270)
t.width(10)
t.circle(100,180)

turtle.done()