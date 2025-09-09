import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor('blue') # Sätter bakgrundsfärgen till blå

t.color('yellow') # Sätter färgen till gul
t.fillcolor("yellow") # Sätter färgen som stjärnan fylls med till gul

for i in range(12): # Skapar en stjärna 12 gånger
    t.penup() # Sätter ner sköldpaddans penna
    t.setheading(i * 30) # Bestämmer positionen av sköldpaddan
    t.forward(100) # Förflyttar sköldpaddan 100 pixlar
    t.pendown() # Sätter upp sköldpaddans penna
    
    t.begin_fill() # Fyller in stjärnan
    for _ in range(5): # Skapar en stjärna 5-gånger
        t.forward(10) # Förflyttar sköldpaddan 10 pixlar
        t.right(126) # Roterar sköldpaddan 126 grader
        t.forward(10) # Förflyttar sköldpaddan 10 pixlar
        t.left(54) # Roterar sköldpaddan 54 grader
    t.end_fill() # Slutar fylla in stjärnan
    
    t.penup() # Sätter ner sköldpaddans penna
    t.backward(100) # Förflyttar sköldpaddan 100 pixlar
    
turtle.hideturtle() # Skjuter sköldpaddan
turtle.done() # Slutar programmet