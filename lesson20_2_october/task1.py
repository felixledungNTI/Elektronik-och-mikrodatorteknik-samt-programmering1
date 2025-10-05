import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.addshape('cartoonMushroom.gif')
t.shape('cartoonMushroom.gif')
t.penup()

t.goto(0,0)

jumpHeight = 50
fallSpeed = 5

def jump():
    if t.ycor() == 0:
        t.sety(jumpHeight)
        fall()
    
def fall():
    y = t.ycor()
    if y > 0:
        y -= fallSpeed
        if y < 0:
            y = 0
        t.sety(y)
        s.ontimer(fall, 20)
    
s.listen()
s.onkey(jump, 'space')

turtle.done()