import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for c in range(5): # Skapar en for-loop som kollar hur mycket fyrkantens sida ska vara och roterar sköldpaddan 90 grader.
    t.forward(25) # Förflyttar sköldpaddan 25 pixlar
    t.left(90) # Roterar sköldpaddan 90 grader
    t.forward(20) # Förflyttar sköldpaddan 20 pixlar
    t.right(90) # Roterar sköldpaddan 90 grader
    
turtle.done()