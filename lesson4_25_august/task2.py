import turtle

s = turtle.getscreen()
t = turtle.Turtle()

#gör en halv triangel
t.forward(300)
t.right(90)
t.backward(150)
t.left(90)

# gör andra halvan av triangeln
t.backward(300)
t.right(90)
t.forward(150)
t.left(90)

turtle.done() # gör så att programmet inte stängs direkt