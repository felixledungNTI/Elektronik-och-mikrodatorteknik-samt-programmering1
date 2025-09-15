import turtle

def movingObject(move):
    move.fillcolor('green')
    move.begin_fill()
    move.circle(20)
    move.end_fill()

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.tracer(0)
    move = turtle.Turtle()
    move.color('green')
    move.speed(0)
    move.width(2)
    move.hideturtle()
    move.penup()
    move.goto(-250,0)
    move.pendown()
    
    while True:
        move.clear()
        movingObject(move)
        screen.update()
        move.forward(0.5)

turtle.done()