from turtle import Screen, Turtle, mainloop

def border():
    border = Turtle(visible=False)
    border.hideturtle()
    border.color('red')
    border.pensize(3)
    border.penup()
    border.goto(-250,-250)
    border.pendown()
    
    for c in range(4):
        border.forward(500)
        border.left(90)

def move():
    x,y = player.pos()
    
    if -250 < x < 250 and -250 < y < 250:
        player.forward(10)
    else:
        player.left(180)
        player.forward(10)

def left():
    player.left(300)

def right():
    player.right(300)
    
def shoot():
    screen.onkey(None,'space')
    if quiver:
        arrow = quiver.pop(0)
    else:
        arrow = Turtle('circle', visible=False)
        arrow.speed(0)
        arrow.color('red')
        arrow.penup()
    arrow.setpos(player.pos())
    arrow.setheading(player.heading())
    flight(arrow)
    arrow.showturtle()
    screen.onkey(shoot, 'space')
    
def flight(arrow):
    if abs(arrow.xcor()) < 250 and abs(arrow.ycor()) < 250:
        arrow.forward(10)
        screen.ontimer(lambda: flight(arrow), 20)
    else:
        arrow.hideturtle()
        quiver.append(arrow)
    
screen = Screen(); screen.setup(500, 500); screen.bgcolor('black')
border()
quiver = []
player = Turtle('turtle')
player.color('green')
player.speed(1)
player.shapesize(1.5)
player.showturtle()
screen.onkey(shoot,'space'); screen.onkey(left,'Left'); screen.onkey(right,'Right')
screen.onkey(move, 'Up')
screen.listen(); mainloop()