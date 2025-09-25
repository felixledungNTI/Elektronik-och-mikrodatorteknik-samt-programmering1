import turtle
import time

s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)

radius = 35 # Skapar en variabel kallad radius som bestämmer radien på cirklarna i trafikljuset, i detta fall 35px (pixlar)
pdg = 10 # Skapar en variabel kallad pdg (förkortning för padding) som bestämmer avståndet mellan trafikljusen, i detta fall 10px (pixlar)
gap = 30 # Skapar en variabel kallad gap som bestämmer avståndet mellan varje cirkel i trafikljuset, i detta fall 30px (pixlar)

# Denna variabel skapar en array (lista) för att sätta posirtionen för varje trafikljus i x och y koordinater.
trafficPos = [[(75, 50), (75, 130), (75, 210)], # Första trafikljuset som får positionen (75, 50), (75, 130) och (75, 210)
              [(225, 50), (225, 130), (225, 210)], # Andra trafikljuset som får positionen (225, 50), (225, 130) och (225, 210)
              [(375, 50), (375, 130), (375, 210)]] # Tredje trafikljuset som får positionen (375, 50), (375, 130) och (375, 210)

text = turtle.Turtle() # Skapar en ny variabel som kallas för 'text'. Text variabeln skapar en ny turtle som används för att skriva ut text i fönstret.
text.hideturtle() # Gömmer själva 'turtle' ikonen så att den inte syns i fönstret
text.color('white') # Sätter färgen på texten till vit
text.penup() # Lyfter pennan för att undvika att rita när den flyttas
text.goto(225, 350) # Flyttar 'turtle' till positionen (225, 350) för att placera texten högst upp i fönstret
text.write('Felixs egna trafikljus', align='center', font=('Courier', 24, 'bold')) # Skriver ut texten 'Felix egna trafikljus'. Texten placeras i mitten av fönstret, men över trafikljusena i fönstret. Texten får bold (fetstil) med storleken 24 pixlar. 

turtle.bgcolor('black') # Sätter bakgrundsfärgen på fönstret till svart

for index, g in enumerate(trafficPos): # Skapar en loop som loopar igenom varje trafikljus i trafficPos arrayen. Jag valde att använda enumerate för att loopa igenom alla trafikljus för att få positionerna för varje trafikljus. Inuti parenteserna definerade jag trafficPos (positionena för varje trafikljus) som g (group) och index (indexet för varje trafikljus i arrayen ovan).
    gIndex = trafficPos[index] # Skapar en variabel som jag har döpt till gIndex. Denna variabel används för att kalla på positionerna för varje trafikljus som finns. Inuti hakparanteserna efter trafficPos valde jag att använda index för att få ut positionern för varje trafikljus i trafficPos arrayen.
    xs = [x for x, y in g] # Skapade en array med variabelns namn 'xs' som tillhandahåller alla x kordinater för varje trafikljus i trafficPos arrayen.
    ys = [y for x, y in g]  # Skapade en array med variabelns namn 'ys' som tillhandahåller alla y kordinater för varje trafikljus i trafficPos arrayen.
    xStart = min(xs) - radius - pdg # Kalkylerar start kordinaten för x axeln i trafikljuset. Kalkylationen görs för att placera trafikljuset korrekt i fönstret.
    yStart = min(ys) - radius - pdg # Kalkylerar start kordinaten för y axeln i trafikljuset. Kalkylationen görs för att placera trafikljuset korrekt i fönstret.

    t.penup() # Lyfter pennan för att undvika att rita när den flyttas
    t.goto(xStart, yStart) # Flyttar 'turtle' till start positionen för varje trafikljus
    t.pendown() # Sänker pennan för att börja rita
    t.pencolor('white') # Sätter färgen på pennan till vit

    width = max(xs) - min(xs) + 2 * radius + 2 * pdg # Räknar ut bredden på trafikljuset
    height = max(ys) - min(ys) + 2 * radius + 2 * pdg # Räknar ut höjden på trafikljuset

    for a in range(2): # Skapar en loop som loopas igenom 2 ggr för att rita trafikljusets rektangel.
        t.forward(width) # Ritar bredden på trafikljuset
        t.left(90) # Vänder 'turtle' 90 grader åt vänster
        t.forward(height) # Ritar höjden på trafikljuset
        t.left(90) # Vänder 'turtle' 90 grader åt vänster

t.color('gray') # Sätter färgen på pennan till grå

def drawLightCircle(trafficPos, color): # Skapar en funktion som ritar cirklarna i trafikljuset. Funktionen har två variabler (parametrar) som är trafficPos och color. TrafficPos hämtar x och y kordinaterna för varje cirkel i trafikljuset. Color bestämmer färgen på cirkeln som ritas.

    x, y = trafficPos[0], trafficPos[1] # Bestämmer x och y kordinaterna för varje cirkel i trafikljuset

    centerY = y # Beräknar mitten av y kordinaten för varje cirkel i trafikljuset

    t.penup() # Lyfter pennan för att undvika att rita när den flyttas
    t.goto(x, y - radius) # Flyttar 'turtle' till positionen (x, y-radius) för att placera cirkeln korrekt i trafikljuset
    t.pendown() # Sänker pennan för att börja rita
    t.color(color) # Sätter färgen på cirkeln till den givna färgen i color variabeln
    t.begin_fill() # Börjar fylla i cirkeln med den givna färgen i color variabeln
    t.circle(radius) # Ritar en cirkel med den givna radien i radius variabeln
    t.end_fill() # Avslutar fyllningen av cirkeln

def resetLight(trafficPos): # Skapar en funktion som resetar alla trafikcirklars färger till grå
    for group in trafficPos: # Skapar en loop som loopar igenom varje trafikljus i trafficPos arrayen
        for pos in group: # Skapar en loop som loopar igenom varje cirkel i varje trafikljus
            drawLightCircle(pos, 'gray') # Anropar drawLightCircle funktionen för att rita varje cirkel i trafikljuset med färgen grå

for i in range(len(trafficPos)): # Skapar en loop som loopar igenom varje trafikljus i trafficPos arrayen
    for j in range(3): # Skapar en loop som loopar igenom varje cirkel i varje trafikljus
        drawLightCircle(trafficPos[i][j], 'gray') # Anropar drawLightCircle funktionen för att rita varje cirkel i trafikljuset med färgen grå

# Skapar en array som innehåller alla färgmönster för alla tre trafikljus
colorCycle = [
            ['red', 'gray', 'gray'], # Första trafikljusets färg som får mönstret röd, grå, grå
            ['gray', 'yellow', 'gray'], # Andra trafikljusets färg som får mönstret grå, gul, grå
            ['gray', 'gray', 'green'] # Tredje trafikljusets färg som får mönstret grå, grå, grön
        ]

while True: # Skapar en oändlig loop som loopar igenom alla trafikljusens färgmönster
    for s in range(3): # Skapar en loop som loopar igenom varje färgmönster i colorCycle arrayen
        for i in range(len(trafficPos)): # Skapar en loop som loopar igenom varje trafikljus i trafficPos arrayen
            for j in range(3): # Skapar en loop som loopar igenom varje cirkel i varje trafikljus
                color = colorCycle[(s+i)%3][j] # Beräknar färgen för varje cirkel i trafikljuset baserat på det nuvarande färgmönstret i colorCycle arrayen
                drawLightCircle(trafficPos[i][j], color) # Anropar drawLightCircle funktionen för att rita varje cirkel i trafikljuset med den beräknade färgen
        time.sleep(2.5) # Pausar färgerna i 2.5 sekunder innan loopen startar om

turtle.done()
