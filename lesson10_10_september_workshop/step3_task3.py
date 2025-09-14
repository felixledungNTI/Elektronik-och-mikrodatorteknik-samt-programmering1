import turtle
import math

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

t.pensize(2.5)

radius1 = 150
radius2 = 95
radius3 = 40
radiusVerySmall = 5

turtle.bgcolor('lightblue')


def grass():
    screenWidth = s.window_width()
    screenHeight = s.window_height()

    t.penup()
    t.goto(-screenWidth // 2, -screenHeight // 2)
    t.pendown()
    t.color('green')
    t.begin_fill()

    for c in range(2):
        t.forward(screenWidth)
        t.left(90)
        t.forward(screenHeight // 4)
        t.left(90)
    t.end_fill()


def treeTrunk(treeX):
    t.fillcolor('brown')
    t.color('brown')
    t.penup()
    t.goto(treeX - 22.5, -s.window_height()//4)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(45)
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(45)
    t.setheading(270)
    t.forward(50)
    t.end_fill()


def treeRight(treeX=450):
    treeTrunk(treeX)
    t.fillcolor('green')
    t.color('green')

    height = math.sin(math.radians(50)) * 100
    width = math.cos(math.radians(50)) * 100

    for c in range(5):
        trunkTop = -s.window_height()//4+50
        y = trunkTop+c*(height/2)
        
        t.penup()
        t.goto(treeX - 100 * math.cos(math.radians(40)), y)
        t.pendown()
        t.begin_fill()
        t.setheading(40)
        t.forward(100)
        t.setheading(-40)
        t.forward(100)
        t.goto(treeX, y)
        t.end_fill()


def treeLeft(treeX=-450):
    treeTrunk(treeX)
    t.fillcolor('green')
    t.color('green')

    height = math.sin(math.radians(50)) * 100
    width = math.cos(math.radians(50)) * 100

    for c in range(5):
        trunkTop = -s.window_height()//4+50
        y = trunkTop+c*(height/2)
        
        t.penup()
        t.goto(treeX + 100 * math.cos(math.radians(40)), y)
        t.pendown()
        t.begin_fill()
        t.setheading(140)
        t.forward(100)
        t.setheading(220)
        t.forward(100)
        t.goto(treeX, y)
        t.end_fill()


def tree(treeX):
    treeTrunk(treeX)
    t.fillcolor('green')

    height = math.sin(math.radians(50)) * 100
    width = math.cos(math.radians(50)) * 100

    t.color('green')

    for c in range(5):
        y = c * (height / 2)

        t.penup()
        t.goto(treeX - 100 * math.cos(math.radians(40)), y)
        t.pendown()
        t.begin_fill()

        t.setheading(40)
        t.forward(100)

        t.setheading(-40)
        t.forward(100)

        t.goto(450, y)

        t.end_fill()

def scarf():
    scarfY = -75+radius2*2
    
    t.setheading(-450)
    t.pencolor('red')
    t.pensize(10)
    t.penup()
    t.goto(-20,scarfY)
    t.pendown()
    t.circle(25, 180)
    t.hideturtle()
    
    t.setheading(270)
    t.pencolor('red')
    t.penup()
    t.goto(30,scarfY)
    t.pendown()
    t.forward(100)

def snowman():
    # body
    t.penup()
    t.pencolor('white')
    t.fillcolor('white')
    t.goto(0, -350)
    t.pendown()
    t.begin_fill()
    t.circle(radius1)
    t.end_fill()

    t.penup()
    t.goto(0, -75)
    t.pendown()
    t.begin_fill()
    t.circle(radius2)
    t.end_fill()

    t.penup()
    t.goto(0, 105)
    t.pendown()
    t.begin_fill()
    t.circle(radius3)
    t.end_fill()

    # hat
    t.setheading(180)
    t.penup()
    t.pencolor('#2e2e2e')
    t.fillcolor('#2e2e2e')
    t.goto(150, 210)
    t.pendown()
    t.begin_fill()
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
    t.right(90)
    t.forward(25)
    t.end_fill()

    scarf()

    # mouth
    t.penup()
    t.pencolor('black')
    t.goto(0, 130)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # eyes
    
    #vänsta ögat
    t.penup()
    t.goto(-20, 155)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    #högra ögat
    t.penup()
    t.goto(15, 155)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    # arm1
    t.pencolor('brown')
    t.pensize(5)
    t.setheading(0)
    t.penup()
    t.goto(95, 30)
    t.pendown()
    t.forward(45)

    t.setheading(35)
    t.penup()
    t.goto(138, 30)
    t.pendown()
    t.forward(25)

    # arm2
    t.setheading(-140)
    t.penup()
    t.goto(-95, 30)
    t.pendown()
    t.forward(45)

    t.setheading(-105)
    t.penup()
    t.goto(-130, 0)
    t.pendown()
    t.forward(25)

    t.hideturtle()

    t.penup()

    t.pencolor('green')
    t.begin_fill()
    t.goto(0, 75)
    t.pendown()
    t.circle(radiusVerySmall)
    t.color('green')
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(0, 50)
    t.pendown()
    t.circle(radiusVerySmall)
    t.color('green')
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(0, 25)
    t.pendown()
    t.circle(radiusVerySmall)
    t.color('green')
    t.end_fill()
    
    t.penup()
    t.begin_fill()
    t.goto(0, 0)
    t.pendown()
    t.circle(radiusVerySmall)
    t.color('green')
    t.end_fill()

def sun():

    t.pencolor('orange')
    t.pensize(5)
    t.penup()
    t.goto(-800, 500)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(100)
    t.end_fill()


grass()
snowman()

treeRight(300)
treeRight(600)
treeRight(750)

treeLeft(-300)
treeLeft(-600)
treeLeft(-750)

sun()

t.hideturtle()

turtle.done()
