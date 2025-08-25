import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.bgcolor("red") # sätter bakgrundsfärgen till röd

#gör en figur
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

turtle.done() # gör så att programmet inte stängs direkt