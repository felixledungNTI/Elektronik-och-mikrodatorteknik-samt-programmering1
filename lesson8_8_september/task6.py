import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def vimpel(x,y, angle, color):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()

    t.begin_fill()
    t.forward(100)
    t.right(100)
    t.forward(40)
    t.right(160)
    t.forward(40)
    t.right(100)
    t.color(color)
    t.end_fill()
    
x = 0
y = 0

t.setheading(90)

vimpel(0,0,90, 'blue')
vimpel(10,65,90,'blue')
vimpel(20,110,90,'blue')
vimpel(30,155,90,'blue')
vimpel(100,0,90, 'red')
vimpel(110,65,90, 'red')
vimpel(120,110,90, 'red')
vimpel(130,155,90, 'red')
vimpel(175,0,90, 'green')
vimpel(185,65,90,'green')
vimpel(195,110,90,'green')
vimpel(205,155,90,'green')

turtle.done()