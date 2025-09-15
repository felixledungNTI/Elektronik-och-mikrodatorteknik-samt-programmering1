import turtle
import time

s = turtle.getscreen()
s.tracer(0)

ball = turtle.Turtle()
square = turtle.Turtle()

radiusCircle = 25

ball.penup()
ball.goto(0,0)
ball.pendown()
ball.color('green')
ball.begin_fill()
ball.circle(radiusCircle)
ball.end_fill()

square.penup()
square.goto(150,-50)
square.pendown()
square.color('red')
square.begin_fill()

def drawingSquare(t, size):
    x = t.xcor()
    y = t.ycor()
    heading = t.heading()
    
    t.penup()
    t.goto(x,y)
    t.setheading(heading)
    t.pendown()
    
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

drawingSquare(square,100)
square.penup()

s.update()

while True:
    # ball
    ball.clear()
    ball.sety(ball.ycor()-2)
    ball.begin_fill()
    ball.circle(radiusCircle)
    ball.end_fill()
    
    # square
    square.clear()
    square.sety(square.ycor()-2)
    drawingSquare(square,100)
    
    s.update()
    time.sleep(0.01)
turtle.hideturtle()

turtle.done()