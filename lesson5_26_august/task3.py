import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor("black") #Sätter bakgrundsfärgen på hela applikationen till svart

# En fyrkant
t.color("red") # Sätter fyrkantens färg till röd
t.begin_fill() # "Start" markerar objektet, som ska fyllas

t.penup() # Tar upp sköldpaddan så att positionen på objektet kan ändras
t.goto(-150, 0) #Anger x och y position för objektet. I detta fall (x: -150, y: 0)
t.setheading(0) #Sätter sköldpaddans position till en specifik vinkel
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till

t.left(90)
t.forward(100)
t.right(90)
t.backward(100)


t.left(90)
t.backward(100)
t.right(90)
t.forward(100)

t.end_fill() # Slutar fylla objektet med färg

# En triangel

t.penup()# Tar upp sköldpaddan så att positionen på objektet kan ändras
t.goto(150,0)  #Anger x och y position för objektet. I detta fall (x: 150, y: 0)
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till

t.color("pink") # Sätter fyrkantens färg till rosa
t.begin_fill() # "Start" markerar objektet, som ska fyllas

#En foorloop som upprepas tre gånger
for i in range(3):
    t.forward(300) #sätter till 300 pixlar
    t.left(120) #Sätter till 120 pixlar
t.end_fill() # Slutar fylla objektet med färg

#En cirkel

t.penup() # Tar upp sköldpaddan så att positionen på objektet kan ändras
t.goto(650,0) #Anger x och y position för objektet. I detta fall (x: 650, y: 0)
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till

t.color("purple") # Sätter fyrkantens färg till lila
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.circle(50) # Sätter cirkels radie till 50 
t.end_fill() # Slutar fylla objektet med färg

turtle.done()