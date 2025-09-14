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

# Första trappan
stepOne = stair(0,0)

# Andra trappan
xTwo = 200
stepTwo = stair(xTwo,0)

# Rita linjer mellan motsvarande steg
for c in range(len(stepOne)):
    leftX1, rightX1 = stepOne[c]
    leftX2, rightX2 = stepTwo[c]
    
    t.penup()
    t.goto(leftX1, rightX1)
    t.pendown()
    t.goto(leftX2, rightX2)

turtle.done()
