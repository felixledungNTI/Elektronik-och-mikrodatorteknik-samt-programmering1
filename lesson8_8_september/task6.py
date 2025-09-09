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

for c in range(4):
    

vimpel(0,0,90, 'blue')
vimpel(0,45,90,'blue')
vimpel(0,90,90,'blue')
vimpel(0,135,90,'blue')
vimpel(75,0,90, 'red')
vimpel(75,45,90, 'red')
vimpel(75,90,90, 'red')
vimpel(75,135,90, 'red')
vimpel(150,0,90, 'green')
vimpel(150,45,90,'green')
vimpel(150,90,90,'green')
vimpel(150,135,90,'green')

turtle.done()