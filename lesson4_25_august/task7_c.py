import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor("green") #bakgrunden är grän
t.color("pink")#objektets färg är rosa

#Skapar första halvan av fyrkanten
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

#Skapar andra halvab av fyrkanten
t.right(90)
t.backward(100)
t.left(90)
t.forward(100)

#Skapar en cirkel med radien 50
t.circle(50)

turtle.done() # gör så att programmet inte stängs direkt