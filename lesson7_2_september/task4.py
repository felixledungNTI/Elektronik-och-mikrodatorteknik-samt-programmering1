import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-240, 150) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -240 och y = 150
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("blue") # Sätter färgen till blå
t.begin_fill() # Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(480) #Sköldpaddan går fram 480 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(300) # Förflyttar sköldpaddan 300 pixlar från startpunkten
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(480) #Sköldpaddan går fram 480 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(300) #Förflyttar sköldpaddan 300 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar sköldpaddan saå att sköldpaddan kan förflytta sig
t.goto(-90, 150) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -90 och y = 150
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("yellow") # Sätter färgen till guld
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(60) #Sköldpaddan går fram 60 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(300) #Förflyttar sköldpaddan 300 pixlar från startpunkten
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(60) #Sköldpaddan går fram 60 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(300) #Förflyttar sköldpaddan 300 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() # Förflyttar sköldpaddan saå att sköldpaddan kan förflytta sig
t.goto(-240, 30) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -240 och y = 30
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska förjas fullas i med färg
t.forward(480) # Sköldpaddan går fram 480 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(60) #Förflyttar sköldpaddan 60 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(480) #Sköldpaddan går fram 480 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(60) #Förflyttar sköldpaddan 60 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

turtle.done()