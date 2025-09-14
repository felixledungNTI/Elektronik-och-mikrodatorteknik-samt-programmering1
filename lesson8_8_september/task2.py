import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0) # Sätter hastigheten på processen till det högsta som är möjligt

def stair(x,y): # Skapar en funktion som skapar en trappa med 7 steg. Definerar x och y.
    t.penup() # Tar upp sköldpaddan
    t.goto(x,y) # Förflyttar sköldpaddan till en viss position
    t.pendown() # Sätter ner sköldpaddan
    positions = [] # Skapar en tom lista för kordinater
    
    for c in range(7): # Skapar en for-loop som kollar hur mycket halva fyrkanten ska vara samt även roterar sköldpaddan 90 grader
        t.forward(25) # Förflyttar sköldpaddan 25 pixlar
        t.left(90) # Roterar sköldpaddan 90 grader
        t.forward(20) # Förflyttar sköldpaddan 20 pixlar
        t.right(90) # Roterar sköldpaddan 90 grader
        positions.append((t.xcor(), t.ycor())) # Förflyttar sköldpaddan 20 pixlar och även lägger till kordinaterna för trappan i listan som kallas för positions
    return positions # Returnerar tillbaka listan som kallas för positions
    
stepOne = stair(0,0) # Skapar en variabel som kallas för stepOne

xTwo = 200 # Skapar en variabel som kallas för xTwo och sätter dess värde till 200

for x,y in stepOne: #Skapar en for-loop som kollar hur mycket halv-fyrkanten ska vara samt roterar även sköldpaddan 90 grader
    t.penup() # Tar upp sköldpaddan
    t.goto(x,y) # Förflyttar sköldpaddan till en viss position
    t.pendown() # Sätter ner sköldpaddan
    t.goto(xTwo,y) # Förflyttar sköldpaddan till en viss position

stair(xTwo,0) # Skapar en funktion som kallas för stair och sätter dess värde till xTwo och 0

turtle.done()
