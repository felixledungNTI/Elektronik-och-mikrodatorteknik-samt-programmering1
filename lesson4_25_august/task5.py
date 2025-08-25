import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor("blue") # ändrade bakgrundsfärg
t.color("red") # ändrade färg på objektet

#en sned figur
t.right(45)
t.forward(180)
t.left(45)
t.backward(180)

t.right(45)
t.backward(180)
t.left(45)
t.forward(180)

#tredje snea figur
t.right(60)
t.forward(180)
t.left(60)
t.backward(180)

t.right(60)
t.backward(180)
t.left(60)
t.forward(180)

#fjärde snea figur
t.right(75)
t.forward(180)
t.left(75)
t.backward(180)

t.right(75)
t.backward(180)
t.left(75)
t.forward(180)

#fjärde snea figur
t.right(75)
t.backward(180)
t.left(75)
t.forward(180)

t.right(75)
t.forward(180)
t.left(75)
t.backward(180)

turtle.done() # gör så att programmet inte stängs direkt