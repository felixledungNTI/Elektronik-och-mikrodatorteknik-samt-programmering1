import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.width(15)
t.speed(5)

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(370, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 370 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("red") # Sätter färgen till röd
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, 180) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(240, -85) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 240 och y = -85
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("green") # Sätter färgen till grön
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, 180) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(110, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 110 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("black") # Sätter färgen till svart
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, 180) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-20, -85) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -20 och y = -85
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("yellow") # Sätter färgen till gul
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, 180) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-150, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -150 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("cyan") # Sätter färgen till cyan
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, 180) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-150, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -150 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("cyan") # Sätter färgen till cyan
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, -180) #Sätter radien på cirkeln till 110 och antal grader den ska ritas till 180 grader (en halvcirkel) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(-20, -85) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = -20 och y = -85
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("yellow") # Sätter färgen till gul
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, -180) #Sätter radien på cirkeln till 110 och antal grader den ska ritas till 180 grader (en halvcirkel) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(110, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 110 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("black") # Sätter färgen till svart
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, -180) #Sätter radien på cirkeln till 110 och antal grader den ska ritas till 180 grader (en halvcirkel) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(240, -85) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 240 och y = -85
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("green") # Sätter färgen till grön
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, -180) #Sätter radien på cirkeln till 110 och antal grader den ska ritas till 180 grader (en halvcirkel) 

t.penup() #Förflyttar pennan så att sköldpaddan kan förflytta sig
t.goto(370, 5) #Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = 370 och y = 5
t.pendown() #Sätter ner pennan där sköldpaddan har förflyttas till
t.color("red") # Sätter färgen till röd
t.setheading(90) #Bestämmer sköldpaddans position, i detta fall till 90 
t.circle(110, -180) #Sätter radien på cirkeln till 110 och antal grader den ska ritas till 180 grader (en halvcirkel)

turtle.done() # Så att programmet ej stängs