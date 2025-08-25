import turtle

s = turtle.getscreen()
t = turtle.Turtle()

# gör streck fram och sedan uppåt
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

# gör tvärtom som ovan
t.right(90)
t.backward(100)
t.left(90)
t.forward(100)

turtle.done() # gör så att programmet inte stängs direkt