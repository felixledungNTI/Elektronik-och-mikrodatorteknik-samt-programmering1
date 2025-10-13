import turtle

wn = turtle.Screen()
wn.setup(600,600)
wn.is_crosses = True

wn.bgcolor('red')

grid = turtle.Turtle()
player = turtle.Turtle()

grid.hideturtle()
player.hideturtle()

def drawLine(startX, startY, endX, endY):
    grid.penup()
    grid.pensize(5)
    grid.setpos(startX, startY)
    grid.pendown()
    grid.setpos(endX, endY)
    
def drawGrid():
    drawLine(-300,100,300,100)
    drawLine(-300,-100,300,-100)
    drawLine(-100,300,-100,-300)
    drawLine(100,300,100,-300)
    
drawGrid()

def drawX():
    player.color('black')
    player.left(45)
    
    for _ in range(4):
        player.forward(140)
        player.forward(-140)
        player.left(90)
        player.right(45)
        
def drawO():
    player.color('black')
    player.dot(150)
    player.color('white')
    player.dot(150)
    
#Show image while clicking in the grid
def drawImage(x,y):
    player.penup()
    player.setpos(x,y)
    player.pendown()
    
    cursor = turtle.addshape('lesson25_13_october/clickAbleCursor.gif')
    player.shape('lesson25_13_october/clickAbleCursor.gif')
    
def draw(x,y):
    player.penup()
    player.setpos(x,y)
    player.pendown()
    
    if wn.is_crosses:
        drawX()
        wn.is_crosses = False
    else:
        drawO()
        wn.is_crosses = True
    wn.onclick(draw)
    
wn.onclick(drawImage)
    
turtle.done()