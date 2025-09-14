import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.shape('turtle') # Sätter sköldpaddans form till en turtle
t.color('red') # Sätter färgen till röd
t.forward(90) # Förflyttar sköldpaddan 90 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.forward(100) # Förflyttar sköldpaddan 100 pixlar
t.dot(20) # Sätter en punkt i sköldpaddans position
t.color('black') # Sätter färgen till svart
t.left(90) # Roterar sköldpaddan 90 grader
t.forward(100) # Förflyttar sköldpaddan 100 pixlar
t.dot(20) # Sätter en punkt i sköldpaddans position
t.left(90) # Roterar sköldpaddan 90 grader
t.forward(100) # Förflyttar sköldpaddan 100 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.right(45) # Roterar sköldpaddan 45 grader
t.penup() # Tar upp sköldpaddan
t.forward(50) # Förflyttar sköldpaddan 50 pixlar
t.pendown() # Sätter ner sköldpaddan

turtle.done()