import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()


t.penup() #Flyttar turtlen till en ny position
t.goto(0,0) #Anger position, i detta fall (x = 0, y = 0)
t.color("red") # sätter cirkelns bakgrundsfärg till grön
t.pendown() # slutar positionerna
t.begin_fill() # börjar fylla i med färg
circle1 = t.circle(50) #Skapar en cirkel med radien 50
t.end_fill() # slutar fylla i med färg

t.penup() #Flyttar turtlen till en ny position
t.goto(10,50) #Anger position, i detta fall (x = 10, y = 50)
t.color("green") # sätter cirkelns bakgrundsfärg till grön
t.pendown() # slutar positionerna
t.begin_fill() # börjar fylla i med färg
circle2 = t.circle(30) #Skapar en cirkel med radien 30
t.end_fill() # slutar fylla i med färg

t.penup() #Flyttar turtlen till en ny position
t.goto(20, 100) #Anger position, i detta fall (x = 20, y = 100)
t.color("blue") # sätter cirkelns bakgrundsfärg till blå
t.pendown() # slutar positionerna
t.begin_fill() # börjar fylla i med färg
circle3 = t.circle(10) #Skapar en cirkel med radien 10
t.end_fill() # slutar fylla i med färg

turtle.done()