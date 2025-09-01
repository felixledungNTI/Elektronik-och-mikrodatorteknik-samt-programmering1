import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.goto(0,0) # Flyttar turtlen till angiven position (x, y) i detta fall x: 0, y: 0
t.down() #Placerar turtlen så att den börjar rita
t.width(15) #Sätter bredden till 15
t.color("blue") #Färgen är blå
t.circle(50) #Skapar en cirkel med radie 50

turtle.done() #Gör så att fönstret inte stängs direkt