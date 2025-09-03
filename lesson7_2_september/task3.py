import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(20)

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(0,0) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 0 och y = 0
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("blue") # Sätter färgen till blå
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100)
t.right(90)
t.backward(180)
t.left(90)
t.backward(100)
t.right(90)
t.forward(180)
t.left(90)
t.end_fill()

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(100,0)
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("yellow") 
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100)
t.right(90)
t.backward(180)
t.left(90)
t.backward(100)
t.right(90)
t.forward(180)
t.left(90)
t.end_fill()

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(200,0)
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("red") 
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(100)
t.right(90)
t.backward(180)
t.left(90)
t.backward(100)
t.right(90)
t.forward(180)
t.left(90)
t.end_fill()

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-5,180)
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.fillcolor("#2e2e2e") 
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.forward(10)
t.right(90)
t.forward(750)
t.right(90)
t.forward(10)
t.right(90)
t.forward(750)
t.right(90)
t.end_fill()

turtle.done()