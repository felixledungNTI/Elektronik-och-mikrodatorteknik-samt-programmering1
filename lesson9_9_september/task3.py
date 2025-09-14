import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.shape('turtle') # Sätter sköldpaddans form till en turtle
t.speed(0) #Ändrar hastigheten till det högsta som är möjligt

def square(storlek, color): # Skapar en fyrkant i en funktion som kallas square. Den definerar storleken och färgen på fyrkanten
    t.fillcolor(color) # Sätter färgen på fyrkanten till antigen ljusgrå eller vit. Hämtar färgen från en for-loop.
    t.begin_fill() # Börjar fylla i fyrkanten med den färg som har hämtats från for-loopen.
    for c in range(4): # Skapar en for-loop som kollar hur mycket fyrkantens sida ska vara och roterar sköldpaddan 90 grader.
        t.forward(storlek) # Förflyttar sköldpaddan 100 pixlar
        t.right(90) # Roterar sköldpaddan 90 grader
    t.end_fill() #Slutar fylla i fyrkanten med färg
    
rader = 7 # Sätter antalet rader till 7
kolumner = 8 # Sätter antalet kolumner till 8
cellStorlek = 100 # Sätter storleken på fyrkanterna till 100

startX = -200 # Skapar en variabel som kallas startX och sätter dess värde till -200
startY = 200 # Skapar en variabel som kallas startY och sätter dess värde till 200
t.penup() # Tar upp sköldpaddan
t.goto(startX,startY) # Flyttar sköldpaddan till startX och startY

for rad in range(rader): # Skapar en for-loop som kollar hur mycket rader och kolumner fyrkanterna ska vara.
    for kolumn in range(kolumner): # Skapar en for-loop som kollar hur mycket rader och kolumner fyrkanterna ska vara.
        t.pendown() # Tar ner sköldpaddan
        color = 'lightgray' if (rad+kolumn)%2 == 0 else 'white' # Skapar en variabel som kallas för color och sätter sedan dess värde till 'ljusblå' eller 'vit' baserat på vad raderna och kolumnerna har för index.
        square(cellStorlek, color) # Skapar en fyrkant med storleken cellStorlek och färgen color
        t.penup() # Tar upp sköldpaddan
        t.forward(cellStorlek) # Förflyttar sköldpaddan 100 pixlar
    t.goto(startX, startY - (rad+1)*cellStorlek) # Flyttar sköldpaddan till startX och startY's värde baserat på raderna och kolumnerna's index.

turtle.done()