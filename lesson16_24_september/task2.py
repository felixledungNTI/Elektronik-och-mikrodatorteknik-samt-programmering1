import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

radius = 35
pdg = 10
gap = 30

turtle.bgcolor('black')

trafficPos = [
    [(75,50),(75,130),(75,210)],
    [(225,50),(225,130),(225,210)],
    [(375,50),(375,130),(375,210)]
]

for g in enumerate(trafficPos):
    xs = [x for x, y in g]
    ys = [y for x, y in g]
    xStart = min(xs)-radius-pdg+g*gap
    yStart = min(ys)-radius-pdg
    
    t.penup()
    t.goto(xStart,yStart)
    t.pendown()
    t.pencolor('white')
    
    width = max(xs)-min(xs)+2*radius+2*pdg
    height = max(ys)-min(ys)+2*radius+2*pdg
    
    for a in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

t.color('gray')

def drawLightCircle(trafficPos, color):
    x, y = trafficPos[0], trafficPos[1] - radius
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
lights=[
    ['red','gray','gray'],
    ['gray','yellow','gray'],
    ['gray','gray','green']
]

def updateLights():
    for b in range(len(trafficPos)):
        trafficLight = trafficPos[b]
        colors = lights[b]
        for c in range(len(trafficLight)):
            lightPos = trafficLight[c]
            color = colors[c]
            drawLightCircle(lightPos,color)

def resetLight(trafficPos):
    for group in trafficPos:
        for pos in group:
            drawLightCircle(pos,'gray')
        
def trafficLight():
    for color in lights:
        for i in range(len(trafficPos)):
            for j in range(len(trafficPos[i])):
                drawLightCircle(trafficPos[i][j],color[j])
            time.sleep(1)

while True:
    trafficLight()

turtle.done()