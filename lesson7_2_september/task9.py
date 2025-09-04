import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor('skyblue')

def filled_circle(radie,color):
    t.color(color,color)
    t.begin_fill()
    t.circle(radie)
    t.end_fill()
    
filled_circle(100, 'red')
filled_circle(95, 'orange')
filled_circle(90, 'yellow')
filled_circle(85, 'green')
filled_circle(80,'blue')
filled_circle(75,'purple')
filled_circle(70,'pink')

turtle.done()