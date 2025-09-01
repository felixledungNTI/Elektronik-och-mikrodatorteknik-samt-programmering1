import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.penup() #Sätter ner sköldpaddans penna
t.goto(-150,0) # Flyttar turtlen till angiven position (x, y) i detta fall x: -150, y: 0
t.pendown() #Tar upp sköldpaddans penna
t.down() #Placerar turtlen så att den börjar rita
t.width(15) #Sätter bredden till 15
t.color("yellow") #Färgen är gul
t.circle(50) #Skapar en cirkel med radie 50

t.penup() #Sätter ner sköldpaddans penna
t.goto(150,0) # Flyttar turtlen till angiven position (x, y) i detta fall x: 150, y: 0
t.pendown() #Tar upp sköldpaddans penna
t.down() #Placerar turtlen så att den börjar rita
t.width(15) #Sätter bredden till 15
t.color("blue") #Färgen är blå
t.circle(50) #Skapar en cirkel med radie 50

t.penup() #Sätter ner sköldpaddans penna
t.goto(450,0) # Flyttar turtlen till angiven position (x, y) i detta fall x: 450, y: 0
t.pendown() #Tar upp sköldpaddans penna
t.down() #Placerar turtlen så att den börjar rita
t.width(15) #Sätter bredden till 15
t.color("red") #Färgen är röd
t.circle(50) #Skapar en cirkel med radie 50

turtle.done() #Gör så att fönstret inte stängs direkt när koden har körts