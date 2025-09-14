import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.color('blue') # Sätter färgen till blå-+

def vimpel(x,y, angle): # Skapar en funktion som kallas för vimpel. Definerar x, y och angle.
    t.penup() # Tar upp sköldpaddan
    t.goto(x,y) # Förflyttar sköldpaddan till en viss position
    t.setheading(angle) # Bestämmer sköldpaddans position baserat på angle.
    t.pendown() # Sätter ner sköldpaddan
    
    t.forward(100) # Förflyttar sköldpaddan 100 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(160) # Roterar sköldpaddan 160 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader

x = 0 # Sätter variablen x värde till 0
y = 0 # Sätter variablen y värde till 0

t.setheading(90) # Sätter sköldpaddans position till 90 grader
vimpel(0,0,0) # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 0, y = 0 och angle = 0
vimpel(-50, 25, 25) # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = -50, y = 25 och angle = 25
vimpel(-100,50, 95) # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = -100, y = 50 och angle = 95

turtle.done()