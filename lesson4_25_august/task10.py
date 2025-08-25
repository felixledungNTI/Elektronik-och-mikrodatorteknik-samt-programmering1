import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor("yellow") #bakgrundsfärgen gul

t.color("pink") #border runt cirkeln. Färgen är rosa.
t.pensize(10) #Storleken är 10px

t.fillcolor("cyan") #cirkelns bakgrundsfärg är cyan
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done() # stänger ej fönstret