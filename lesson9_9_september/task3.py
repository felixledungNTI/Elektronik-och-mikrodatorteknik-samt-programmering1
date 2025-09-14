import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.shape('turtle')
t.speed(0)

def square(storlek, color):
    t.fillcolor(color)
    t.begin_fill()
    for c in range(4):
        t.forward(storlek)
        t.right(90)
    t.end_fill()
    
rader = 7
kolumner = 8
cellStorlek = 100

startX = -200
startY = 200
t.penup()
t.goto(startX,startY)

for rad in range(rader):
    for kolumn in range(kolumner):
        t.pendown()
        color = 'lightgray' if (rad+kolumn)%2 == 0 else 'white'
        square(cellStorlek, color)
        t.penup()
        t.forward(cellStorlek)
    t.goto(startX, startY - (rad+1)*cellStorlek)

turtle.done()