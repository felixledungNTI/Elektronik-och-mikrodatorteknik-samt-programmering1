import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(20)

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(0,0) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 0 och y = 0
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("blue") # Sätter färgen till blå
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100)  # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.backward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.backward(100) # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90)  # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(100,0) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 100 och y = 0
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("yellow") # Sätter färgen till gul
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100) # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.backward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.backward(100) # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(200,0) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 200 och y = 0
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("red") # Sätter färgen till röd
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100) # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.backward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.backward(100) # Förflyttar sköldpaddan 100 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(180) # Förflyttar sköldpaddan 180 pixlar
t.left(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-5,180) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -5 och y = 180
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("#2e2e2e") # Sätter färgen till svart
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(10) # Förflyttar sköldpaddan 10 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(750) # Förflyttar sköldpaddan 750 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(10) # Förflyttar sköldpaddan 10 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.forward(750) # Förflyttar sköldpaddan 750 pixlar
t.right(90) # Roterar sköldpaddan 90 grader
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() # Förflyttar pennan för att sköldpaddan kan förflytta sig
t.goto(150, 200) # Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 150 och y = 200
t.write("My flag", align="center", font=("Arial", 20, "normal")) # Skriver ut texten "My flag" i en viss position (x, y) i detta fall x = 150 och y = 200
t.pendown() # Sätter ner pennan för att sköldpaddan har förflyttas till

turtle.done()