import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)


def stair(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    positions = []
    
    for c in range(7):
        t.forward(25)
        t.left(90)
        t.forward(20)
        t.right(90)
        positions.append((t.xcor(), t.ycor()))
    return positions
    
stepOne = stair(0,0)

xTwo = 200

for x,y in stepOne:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.goto(xTwo,y)

stair(xTwo,0)

turtle.done()
