import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.hideturtle()
turtle.bgcolor('black')
t.color('white')

def counter():
    number = 0
    
    #räkna upp till 100
    while number <= 100:
        t.write(number, align='center', font=('Courier', 24, 'normal'))
        t.clear()
        time.sleep(0.5)
        number+=1
    
counter()
turtle.done()