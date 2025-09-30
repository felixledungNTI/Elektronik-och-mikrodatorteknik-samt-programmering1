import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor('#21a1fc')
t.speed(0)
t.hideturtle()

screenWidth = s.window_width()
screenHeight = s.window_height()

#grass
def grass():
    t.penup()
    t.goto(-screenWidth // 2, -screenHeight // 2)
    t.pendown()
    t.color('green')
    t.begin_fill()
    
    for c in range(2):
        t.forward(screenWidth)
        t.left(90)
        t.forward(screenHeight//4)
        t.left(90)
    t.end_fill()
    
def road():
    roadHeight = screenHeight//2
    roadWidth = screenWidth//8
    
    x = -roadWidth//2
    y = -screenHeight//2
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('gray')
    t.begin_fill()
      
    for c in range(2):
        t.forward(roadWidth)
        t.left(90)
        t.forward(roadHeight//2)
        t.left(90)
    t.end_fill()

def house():
    width = 200
    height = 250
    
    x = -screenWidth//8
    y = -screenHeight//4
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('#fce2c4')
    t.begin_fill()
    
    for c in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    
def window(xOffset):
    houseX = -screenWidth
    houseY = -screenHeight//4
    
    windowWidth = 50
    windowHeight = 50
    
    x = xOffset
    y = houseY+150

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('white')
    t.begin_fill()
    
    for c in range(2):
        t.forward(windowWidth)
        t.left(90)
        t.forward(windowHeight)
        t.left(90)
    t.end_fill()

def sun(radius):
    t.penup()
    t.goto(-screenWidth//2+100,screenHeight//2-120)
    t.pendown()
    t.color('yellow')
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
def door():
    houseWidth = 200
    doorWidth = 50
    doorHeight = 75
    
    x = -screenWidth//8+(houseWidth-doorWidth)/2
    y = -screenHeight//4
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color('red')
    t.begin_fill()
    
    for b in range(2):
        t.forward(doorWidth)
        t.left(90)
        t.forward(doorHeight)
        t.left(90)
    t.end_fill()
    
    # door lever
    
    t.penup()
    t.goto(x+10,y+doorHeight/2)
    t.pendown()
    t.color('black')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
#ceiling
def ceiling():
    houseWidth = 200
    houseHeight = 250
    houseX = -screenWidth//8
    houseY = -screenHeight//4
    
    t.penup()
    t.goto(houseX,houseY+houseHeight)
    t.pendown()
    t.color('brown')
    t.begin_fill()
    
    t.goto(houseX - 20, houseY + houseHeight)
    t.goto(houseX + houseWidth/2, houseY + houseHeight + 100)
    t.goto(houseX + houseWidth + 20, houseY + houseHeight)
    t.goto(houseX - 20, houseY + houseHeight)
    t.end_fill()
   
def chimeny():
    houseWidth = 200
    houseHeight = 250
    houseX = -screenWidth//8
    houseY = -screenHeight//4
    
    x = houseX+houseWidth*0.65
    y = houseY+houseHeight+60
    
    chimenyWidth = 20
    chimenyHeight = 40
    
    t.penup() 
    t.goto(x,y)
    t.pendown()
    t.color('brown')
    t.begin_fill()
    
    for p in range(2):
        t.forward(chimenyWidth)
        t.left(90)
        t.forward(chimenyHeight)
        t.left(90)
    t.end_fill()
    
def cloud():
    t.penup()
    t.goto(-200,200)
    t.pendown()
    t.color('white')
    t.begin_fill()
    
    for p in range(2):
        t.circle(50,90)
        t.circle(25,90)
    t.end_fill()
    

grass()
road()
house()
window(30)
window(-70)
sun(50)
door()
ceiling()
chimeny()
cloud()

turtle.done()