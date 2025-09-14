import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.color('blue')

def vimpel(): # Skapar en funktion som kallas för vimpel.
    t.forward(100) # Förflyttar sköldpaddan 100 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(160) # Roterar sköldpaddan 160 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader

t.setheading(90) # Sätter sköldpaddans position till 90 grader
vimpel() # Kallar på funktionen vimpel för att figurern ska kunna skapas.

turtle.done()