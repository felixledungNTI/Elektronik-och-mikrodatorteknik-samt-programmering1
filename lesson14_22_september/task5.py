from turtle import Screen, Turtle, mainloop

def left():
    player.left(300)
def right():
    player.right(300)
def shoot():
    screen.onkey(None,'space')
    if quiver:
        arrow = quiver.pop(0)
    else:
        arrow = Turtle('circle',visible=False)
        arrow.speed('fastest')
        arrow.color('red')
        arrow.penup-7
    arrow.setposition(player.position())
    arrow.setheading(player.heading())
    flight(arrow)
    arrow.showturtle()
    screen.onkey(shoot,'space')
    
def flight(arrow):
    if arrow.distance(0,0)<325:
        arrow.forward(10)
        screen.ontimer(lambda a=arrow: flight(a), 10)
    else:
        arrow.hideturtle()
        quiver.append(arrow)
        
screen = Screen()
screen.setup(500,500)
screen.bgcolor('black')
quiver = []
player = Turtle('turtle')
player.color('green')
player.speed('fastest')
screen.onkey(shoot,'space')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.listen()
mainloop()