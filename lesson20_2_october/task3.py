import turtle
import time
import random

delay = 0.1
score = 0

# Sätter up skärmen för spelet
wn = turtle.Screen() # Skapar spelfönstret
wn.bgcolor('black') # Sätter bakgrundsfärgen på fönstret till svart
wn.setup(width=600, height=600) # Bestämmer storleken på fönstret vilket är 600x600px (pixlar)
wn.tracer(0) # Låter spelet att inte uppdateras automatiskt

# Kod för hiuvudet
head = turtle.Turtle() # Skapar en ny variabel som jag har döpt till head. Variabeln skapar en ny turtle, detta för att skapa huvudet i spelet.
head.speed(0) # Sätter hastigheten på huvudet till det snabbaste som är möjligt
head.shape('square') # Sätter formen till en kvadrat
head.color('green') # Anger färgen till grön
head.shapesize(stretch_wid=0.9, stretch_len=0.9) #Gör huvudet lite smalare än en kvadrat. Kvadraten blir smalare, men också lite avlång.
head.penup() # Lyfter pennan för att undvika att rita nära huvudet
head.goto(0, 0) # Flyttar huvudet till 0, 0
head.direction = 'stop' # Sätter huvudets riktning till 'stop'

food = turtle.Turtle() # Skapar en ny variabel som jag har döpt till food. Variabeln skapar en ny turtle, detta för att skapa maten i spelet.
food.speed(0) # Sätter hastigheten på maten till det snabbaste som är möjligt
food.shape('circle') # Sätter formen på matentill en cirkel
food.color('red') # Anger färgen på mat-cirkeln till röd
food.penup() # Lyfter pennan för att undvika att rita nära maten
food.goto(0, 100) # Flyttar maten till 0, 100

segments = [] # Skapar en ny variabel som heter segments. Variabeln innehåller en array som sparar alla nya 'kuber' i ormen. Koden skapar som små kuber när ormen äter

scoreBoard = turtle.Turtle() # Skapar en ny variabel som heter scoreBoard. Denna variabel skapas för att kunna skriva ut text i spelet. I detta fall poängen
scoreBoard.speed(0) # Sätter hastigheten på scoreBoard till det snabbaste som är möjligt
scoreBoard.color('white') # Sätter färgen på text till vit
scoreBoard.penup() # Lyfter pennan för att undvika att rita nära scoreBoard
scoreBoard.hideturtle() # Gör 'turtle' osynlig
scoreBoard.goto(0, 260) # Sätter positionen till 0, 260
scoreBoard.write('Score: 0', align='center', font=('Arial', 24, 'normal')) # Skriver ut 'Score: 0' centrerat i spelet, med storleken 24px

gameOver = turtle.Turtle() # Skapar en ny variabel som heter gameOver. Denna variabel skriver ut när spelet är över eller slut.
gameOver.speed(0) # Anger hastigheten till den snabbaste som är möjligt
gameOver.color('red') # Sätter färgen på texten till röd
gameOver.penup() # Lyfter pennan för att undvika att rita nära gameOver
gameOver.hideturtle() # Gör 'turtle' osynlig

def up(): # Skapar en funktion som heter up. Funktionen låter huvudet röras uppåt
    if head.direction != 'down': # Om huvudet inte rörs nedåt, så rörs det uppåt istället
        head.direction = 'up' # Sätter huvudets riktning till 'up'

def down(): # Skapar en funktion som heter down. Funktionen låter huvudet röras nedåt
    if head.direction != 'up': # Om huvudet inte rörs uppåt, så rörs det nedåt istället
        head.direction = 'down' # Sätter huvudets riktning till 'down'

def left(): # Skapar en funktion som heter left. Funktionen låter huvudet röras vänster
    if head.direction != 'right': # Om huvudet inte rörs åt höger håll, så rörs det till vänster istället
        head.direction = 'left' # Sätter huvudets riktning till 'left'

def right(): # Skapar en funktion som heter right. Funktionen låter huvudet röras åt höger sida
    if head.direction != 'left':  # Om huvudet inte rörs till vänster, så rörs det åt höger håll istället
        head.direction = 'right' # Sätter huvudets riktning till 'right'

def move():  # Skapar en funktion som heter move. Funktionen flyttar huvudet beroende på huvudets riktning
    if head.direction == 'up': # Om huvudet rörs uppåt, flyttas huvudet upp 20 pixlar
        head.sety(head.ycor() + 20) # Sätter huvudets y-koordinat till huvudets y-koordinat plus 20
    if head.direction == 'down': # Om huvudet rörs nedåt, flyttas huvudet ner 20 pixlar
        head.sety(head.ycor() - 20) # Sätter huvudets y-koordinat till huvudets y-koordinat minus 20
    if head.direction == 'left': # Om huvudet rörs vänster, flyttas huvudet vänster 20 pixlar
        head.setx(head.xcor() - 20) # Sätter huvudets x-koordinat till huvudets x-koordinat minus 20
    if head.direction == 'right': # Om huvudet rörs höger, flyttas huvudet höger 20 pixlar
        head.setx(head.xcor() + 20) # Sätter huvudets x-koordinat till huvudets x-koordinat plus 20

def updateScore(): # Skapar en funktion som heter updateScore. Funktionen uppdaterar scoreBoard
    scoreBoard.clear() # Rensar scoreBoard, ifall någon text redan har skrivits ut i scoreBoardet
    scoreBoard.write('Score: {}'.format(score), align='center', font=('Arial', 24, 'normal')) # Skriver ut poängen. Poängen uppdateras dynamiskt

def resetGame(): # Skapar en funktion som heter resetGame. Funktionen startar om spelet
    global score, segments # Skapar två nuya variablar som heter score och segments. Dessa variablar kan används i hela programmet, det är därför jag har använt global
    head.goto(0, 0) # Flyttar huvudet till 0, 0
    head.direction = 'stop' # Sätter huvudets riktning till 'stop'
    head.showturtle() # Visar huvudet
    for seg in segments: # Loopar igenom alla segmenter (alla kuber i ormen)
        seg.hideturtle() # Gör alla kuber osynliga
    segments.clear() # Rensar ormen
    score = 0 # Sätter poängen till 0
    updateScore() # Uppdaterar scoreBoard
    food.goto(0, 100) # Flyttar maten till 0, 100

wn.listen() # Gör så att fönstret kan lyssna på tangenter
wn.onkeypress(up, 'w') # När 'w' tangenten trycks ner, anropas funktionen up
wn.onkeypress(down, 's') # När 's' tangenten trycks ner, anropas funktionen down
wn.onkeypress(left, 'a') # När 'a' tangenten trycks ner, anropas funktionen left
wn.onkeypress(right, 'd') # När 'd' tangenten trycks ner, anropas funktionen right

food_timer = time.time() # Har skapat en funktion som heter food_timer. Hämtar en tid för att kunna sätta en ny position på maten

while True:  # Skapar en while-loop som loopas när spelet är aktivt. Används för att kunna spela spelet och uppdatera spelet
    wn.update()  # Uppdaterar spelet
    if time.time() - food_timer > 10: # Om maten har väntat i sekunder som har angetts, sätts en ny position på maten
        x = random.randint(-14, 14) * 20 # Skapar ett slumpat tal mellan -14 och 14, och multiplikas med 20. Detta för att få maten att vara på ett heltals-position i spelet
        y = random.randint(-14, 14) * 20 # Skapar ett slumpat tal mellan -14 och 14, och multiplikas med 20. Detta för att få maten att vara på ett heltals-position i spelet
        food.goto(x, y) # Flyttar maten till den slumpade positionen
        food_timer = time.time() # Sätter en ny tid för att kunna sätta en ny position på maten

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: # Om huvudet ligger utanfor fönstret, avslutas spelet
        gameOver.goto(0, 0) # Flyttar gameOver till 0, 0
        gameOver.write('Game Over', align='center', font=('Arial', 36, 'bold')) # Skriver ut 'Game Over' centrerat i spelet, med storleken 36px
        head.hideturtle() # Gör huvudet osynligt
        for s in segments: # Loopar igenom alla segmenter (alla kuber i ormen)
            s.hideturtle() # Gör alla kuber osynliga
        segments.clear() # Rensar ormen
        wn.update() # Uppdaterar spelet
        
        for i in range(5, 0, -1): # Loopar igenom alla tal mellan 5 och 1, med ett steg tillbaka
            gameOver.goto(0,-40)  # Flyttar gameOver till 0, -40
            gameOver.write('Restart in '+str(i), align='center', font=('Arial', 24, 'normal')) # Skriver ut 'Restart in '+str(i) centrerat i spelet, med storleken 24px
            wn.update() # Uppdaterar spelet
            time.sleep(1) # Väntar 1 sekund
            gameOver.clear() # Rensar gameOver
            
        time.sleep(5) # Väntar 5 sekunder
        gameOver.clear() # Rensar gameOver
        resetGame() # Anropar funktionen resetGame

    if head.distance(food) < 25: # Om huvudet har kolliderat med maten med en radius av 25px, sätts en ny position på maten
        x = random.randint(-14, 14) * 20  # Skapar ett slumpat tal mellan -14 och 14, och multiplikas med 20. Detta för att få maten att vara på ett heltals-position i spelet
        y = random.randint(-14, 14) * 20  # Skapar ett slumpat tal mellan -14 och 14, och multiplikas med 20. Detta för att få maten att vara på ett heltals-position i spelet
        food.goto(x, y)  # Flyttar maten till den slumpade positionen
        food_timer = time.time() # Sätter en ny tid för att kunna sätta en ny position på maten
        newSegment = turtle.Turtle()  # Skapar en ny variabel som jag har döpt till newSegment. Variabeln skapar en ny turtle, detta för att skapa en ny segment i ormen
        newSegment.speed(0) # Sätter hastigheten på newSegment till det snabbaste som är möjligt
        newSegment.shape('square') # Sätter formen på newSegment till en kvadrat
        newSegment.color('green') # Anger färgen på newSegment till grön
        newSegment.shapesize(stretch_wid=0.9, stretch_len=0.9) # Gör newSegment avlång och smal
        newSegment.penup() # Lyfter pennan för att undvika att rita nära newSegment
        if segments: # Om segments finns
            last = segments[-1] # Sätter last till det sista elementet i segments
            newSegment.goto(last.xcor(), last.ycor()) # Flyttar newSegment till det sista elementets x och y-koordinater
        else: # Om segments inte finns
            if head.direction == 'up': # Om huvudet rörs uppåt
                newSegment.goto(head.xcor(), head.ycor() - 20) # Flyttar newSegment till huvudets x och y-koordinater plus ett steg uppåt
            elif head.direction == 'down': # Om huvudet rörs nedåt
                newSegment.goto(head.xcor(), head.ycor() + 20) # Flyttar newSegment till huvudets x och y-koordinater minus ett steg nedåt
            elif head.direction == 'left': # Om huvudet rörs vänster sida
                newSegment.goto(head.xcor() + 20, head.ycor()) # Flyttar newSegment till huvudets x och y-koordinater minus ett steg vänsteråt
            elif head.direction == 'right': # Om huvudet rörs åt höger sida
                newSegment.goto(head.xcor() - 20, head.ycor()) # Flyttar newSegment till huvudets x och y-koordinater plus ett steg högeråt
        segments.append(newSegment) # Lägger till newSegment i segments
        score += 2 # Lägger till 2 till poängen
        updateScore() # Uppdaterar scoreBoard

    for index in range(len(segments) - 1, 0, -1):  # Loopar igenom alla segmenter i ormen, startar med sista elementet och går tillbaks till det andra elementet
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor()) # Flyttar segmenten till det andra elementets x och y-koordinater
    if segments: # Om segments finns
        segments[0].goto(head.xcor(), head.ycor()) # Flyttar segmenten till huvudets x och y-koordinater

    move() # Anropar funktionen move
    time.sleep(delay) # Väntar i antal sekunder som har angets i delay variabeln
    wn.update() # Uppdaterar skärmen

wn.mainloop()