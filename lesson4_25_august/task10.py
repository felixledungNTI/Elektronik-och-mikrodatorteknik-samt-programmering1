import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s._color("yellow")

t.color("pink")
t.pensize(10)

t.fillcolor("cyan") 
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done() # stänger ej fönstret