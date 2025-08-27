import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor("cyan") # Sätter bakgrundsfärgen på hela applikationen till cyan

t.penup()# Tar upp sköldpaddan så att positionen på objektet kan ändras
t.goto(0,-250) #Anger x och y position för objektet. I detta fall (x: -150, y: 0)
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.color("black") # Sätter cirkelns färg till svart
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.circle(250) # Sätter cirkelns radie till 250
t.end_fill() # Slutar fylla objektet med färg

t.penup() # Tar upp sköldpaddans så att positionen på objektet kan ändras
t.goto(0,-200) # Anger x och y position för objektet. I detta fall (x: 0, y: -200)
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.color("blue") # Sätter cirkelns färg till blå
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.circle(200) # Sätter cirkelns radie till 200
t.end_fill() # Slutar fylla objektet med färg

t.penup() # Tar upp sköldpaddans så att positionen på objektet kan Ändras
t.goto(0,-150) # Anger x och y position för objektet. I detta fall (x: 0, y: -150)
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.color("red")  # Sätter cirkelns färg till röd
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.circle(150) # Sätter cirkelns radie till 150
t.end_fill() # Slutar fylla objektet med färg

t.penup() # Tar upp sköldpaddans så att positionen på objektet kan Ändras
t.goto(0,-100) # Anger x och y position för objektet. I detta fall (x: 0, y: -100)
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.color("yellow") # Sätter cirkelns färg till guld
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.circle(100) # Sätter cirkelns radie till 100
t.end_fill() # Slutar fylla objektet med färg

turtle.done()