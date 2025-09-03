import turtle

s = turtle.getscreen()
t = turtle.Turtle()

radius = 90

t.penup()#Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(0,0)#Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 0 och y = 0
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.circle(radius) # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 90
t.color("green") #Sätter cirkelns färg till grön
t.end_fill() #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(100,-200)#Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 100 och y = -200
t.pendown()#Sätter ner pennan där sköldpaddan har förflyttas till
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.circle(radius)  # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 90
t.color("blue") # Sätter cirkelns färg till blå
t.end_fill()  #Slutar fylla i cirkeln med färg

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-100,-200)#Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -100 och y = -200
t.pendown()#Sätter ner pennan där sköldpaddan har förflyttas till
t.begin_fill() #Hämtar startpunken för cirkeln, där den ska börjas fullas i med färg
t.circle(radius)  # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är 90
t.color("red") #Sätter färgen till röd
t.end_fill()  #Slutar fylla i cirkeln med färg

turtle.done()