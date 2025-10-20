import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)

def hexagone(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)
        
hexagone(50)

turtle.done()