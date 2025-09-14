import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def vimpel(x,y, angle, color): # Skapar en funktion som kallas för vimpel. Definerar x, y, angle och color.
    t.penup() # Tar upp sköldpaddan
    t.goto(x,y) # Förflyttar sköldpaddan till en viss position
    t.setheading(angle) # Bestäms sköldpaddans position baserat på angle.
    t.pendown() # Sätter ner sköldpaddan

    t.begin_fill() # Fyller in fönstret
    t.forward(100) # Förflyttar sköldpaddan 100 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(160) # Roterar sköldpaddan 160 grader
    t.forward(40) # Förflyttar sköldpaddan 40 pixlar
    t.right(100) # Roterar sköldpaddan 100 grader
    t.color(color) # Sätter färgen till color
    t.end_fill() # Fyller in fönstret
    
x = 0 # Sätter variablen x värde till 0
y = 0

t.setheading(90) # Sätter sköldpaddans position till 90 grader

vimpel(0,0,90, 'blue') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 0, y = 0, angle = 90 och color till blå
vimpel(10,65,90,'blue') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 10, y = 65, angle = 90 och color till blå
vimpel(20,110,90,'blue') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 20, y = 110, angle = 90 och color till blå
vimpel(30,155,90,'blue') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 30, y = 155, angle = 90 och color till blå
vimpel(100,0,90, 'red') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 100, y = 0, angle = 90 och color till röd
vimpel(110,65,90, 'red') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 110, y = 65, angle = 90 och color till röd
vimpel(120,110,90, 'red') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 120, y = 110, angle = 90 och color till röd
vimpel(130,155,90, 'red') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 130, y = 155, angle = 90 och color till röd
vimpel(175,0,90, 'green') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 175, y = 0, angle = 90 och color till grön
vimpel(185,65,90,'green') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 185, y = 65, angle = 90 och color till grön
vimpel(195,110,90,'green') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 195, y = 110, angle = 90 och color till grön
vimpel(205,155,90,'green') # Kallar på funktionen vimpel för att figurern ska kunna skapas. Sätter x = 205, y = 155, angle = 90 och color till grön

turtle.done()