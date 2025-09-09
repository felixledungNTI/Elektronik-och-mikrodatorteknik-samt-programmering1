import turtle

s = turtle.getscreen()
t = turtle.Turtle()

radius = 50 # Sätter radien till 50
width = 15 # Sätter bredden till 15

t.pensize(width) # Sätter bredden på pennan till variabeln width
t.color("black", "blue") # Sätter färgen till svart och blå


t.penup() # Tar upp sköldpaddan för att positionen på objektet kan ändras
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.goto(0,-radius) # Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 0 och y = -radius
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.circle(radius) # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 50
t.end_fill() # Slutar fylla objektet med färg

t.penup() # Tar upp sköldpaddan för att positionen på objektet kan Ändras
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.goto(190,-radius) # Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 190 och y = -radius
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.circle(radius) # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 50
t.end_fill() # Slutar fylla objektet med färg

t.penup() # Tar upp sköldpaddan för att positionen på objektet kan Ändras
t.begin_fill() # "Start" markerar objektet, som ska fyllas
t.goto(380,-radius) # Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 380 och y = -radius
t.pendown() # Sätter ner sköldpaddan på den position objektet har flyttats till
t.circle(radius) # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 50
t.end_fill() # Slutar fylla objektet med färg

turtle.done()