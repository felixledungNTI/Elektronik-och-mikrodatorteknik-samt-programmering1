import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for c in range(16): # Skapar en for-loop som skapar linjer för den figur som fanns i uppgiften. Jag satte värdet i c till 16.
    t.forward(10+5*c) # Förflyttar sköldpaddan till en viss position
    t.left(90) # Roterar sköldpaddan 90 grader
    
turtle.done()