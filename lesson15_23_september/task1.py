import turtle
import time
from datetime import datetime
import math

screen = turtle.Screen() # Skapar ett fönstret för den analoga klocka
screen.setup(width=800, height=800) # Bestämmer storleken på fönstret, i detta fall 800x800
screen.tracer(0) # Avslutar automatisk uppdatering av skärm

viewer = turtle.Turtle() # Skapar en "turtle" för att visa klockans visare
viewer.hideturtle() # Gömmer "turtle" ikonen
viewer.speed(0) # Sätter hastigheten på "turtle" till den snabbaste

clockViewer = turtle.Turtle() # Skapar en "turtle" för att rita klockans 'cirkel'
clockViewer.speed(0) # Sätter hastigheten på "turtle" till den snabbaste
clockViewer.pensize(3) # Sätter tjockleken på pennan till 3

textViewer = turtle.Turtle() # Skapar en "turtle" för att visa den digitala tiden
textViewer.hideturtle() # Gömmer "turtle" ikonen
textViewer.penup() # Lyfter pennan för att undvika att rita när den flyttas
textViewer.goto(0,-250) # Flyttar "turtle" till positionen (0,-250)

titleViewer = turtle.Turtle() # Skapar en "turtle" för att visa titeln på klockan, i detta fall "Analog Klocka"
titleViewer.hideturtle() # Gömmer "turtle" ikonen
titleViewer.penup() # Lyfter pennan för att undvika att rita när den flyttas
titleViewer.goto(0,300) # Flyttar "turtle" till positionen (0,300)
titleViewer.write('Analog Klocka', align='center', font=('Courier', 30)) # Printar titeln på klockan med texten 'analog klocka så att den skrivs ut på fönstret

def drawClock(clockviewer,radius): # Skapar en funktion för att rita klockan. Sätter in två parametrar (variabler), vilket är clockviewer samt radius
    clockviewer.penup() # Lyfter pennan för att undvika att rita när den flyttas
    clockviewer.goto(0,-radius) # Flyttar "turtle" till positionen (0,-radius)
    clockviewer.pendown() # Sänker pennan för att börja rita
    clockviewer.circle(radius) # Ritar en cirkel med den givna radien
    
    for i in range(12): # Skapar en loop som loopas 12 ggr, en gång för varje timme på klockan (1-12)
        angle = i*30 # Beräknar vinkeln för varje timme på klockan (30 grader per timme)
        number = (i+11)%12 + 1 # Beräknar timmarnas nummer (1-12) för att placera dem korrekt på klockan
        x = (radius-40)*math.cos(math.radians(90-angle)) # Beräknar x-koordinaten för varje timmes nummer
        y = (radius-40)*math.sin(math.radians(90-angle)) # Beräknar y-koordinaten för varje timmes nummer
        clockviewer.penup() # Lyfter pennan för att undvika att rita när den flyttas
        clockviewer.goto(x,y-10) # Flyttar "turtle" till positionen (x,y-10) för att placera timmarnas nummer
        
        clockviewer.write(number, align='center', font=('Courier', 16, 'normal')) # Skriver ut timmarnas nummer på klockan

    for c in range(12): # Skapar en loop som loopas 12 ggr, en gång för varje timme på klockan (1-12) för att skapa tim'linjer' (markeringar)
        angle = c*30 # Beräknar vinkeln för varje timme på klockan (30 grader per timme)
        xStart = (radius-15)*math.cos(math.radians(90-angle)) # Beräknar start x-koordinaten för varje timmes linje
        yStart = (radius-15)*math.sin(math.radians(90-angle)) # Beräknar start y-koordinaten för varje timmes linje
        xEnd = radius*math.cos(math.radians(90-angle)) # Beräknar slutet på x-koordinaten för varje timmes linje
        yEnd = radius*math.sin(math.radians(90-angle)) # Beräknar slutet på y-koordinaten för varje timmes linje
        
        clockviewer.penup() # Lyfter pennan för att undvika att rita när den flyttas
        clockviewer.goto(xStart,yStart) # Flyttar "turtle" till start positionen för varje timmes linje
        clockviewer.pendown() # Sänker pennan för att börja rita
        clockviewer.goto(xEnd,yEnd) # Ritar linjen från start positionen till slut positionen

def timeViewer(clockViewer, angle, color, length=180): # Skapar en funktion för att rita vinklar i klockan
    clockViewer.penup() # Lyfter pennan för att undvika att rita för att undvika att rita för att undvika att rita
    clockViewer.home() # Flyttar "turtle" till positionen (0,0)
    clockViewer.color(color) # Sätter färgen på vinklarna
    clockViewer.pensize(3) # Sätter tjockleken på pennan till 3
    clockViewer.pendown() # Sänker pennan för att börja rita
    clockViewer.setheading(90-angle) # Sätter vinkeln för vinklarna
    clockViewer.forward(length) # Ritar vinklarna
    
drawClock(clockViewer,200) # Ritar klockan

while True: # Skapar en loop som loopas endast en gång
    viewer.clear() # Rensar klockans visare
    currentTime = datetime.now() # Beräknar nuvarande tid
    hour = currentTime.hour # Beräknar timmarna
    minutes = currentTime.minute # Beräknar minutrarna
    second = currentTime.second # Beräknar sekundrarna

    textViewer.clear() # Rensar den digitala tiden
    textViewer.write(f'{hour:02d}:{minutes:02d}:{second:02d}', align='center', font=('Courier', 24, 'normal')) # Skriver ut den digitala tiden (ex. 08:10:05). Varför jag använder :02d är för att visa två siffror, även om det xempelvis endast är 5, visas då 05 istället
    
    hour_angle = (hour % 12) * 30 + (minutes / 60) * 30 # Beräknar timmarnas vinkel (30 grader per timme + 0.5 grader per minut)
    minute_angle = (minutes / 60) * 360 # Beräknar minutarnas vinkel (6 grader per minut)
    second_angle = (second / 60) * 360 # Beräknar sekundarnas vinkel (6 grader per sekund)
    
    timeViewer(viewer, hour_angle, 'gray', 100) # Ritar timmarnas vinkel med färgen blå och längden 100
    timeViewer(viewer, minute_angle, 'gray', 150) # Ritar minutarnas vinkel med färgen grön och längden 150
    timeViewer(viewer, second_angle, 'red', 120) # Ritar sekundarnas vinkel med färgen röd och längden 180
    
    screen.update() # Uppdaterar skärmen med den nya tiden
    time.sleep(1) # Pausar programmet i 1 sekund innan loopen startar om

turtle.done()