import turtle

wn = turtle.Screen() # Skapar ett fönster för ping pong spelet
wn.title('Ping Pong Spel') # Spelet får fönster titeln 'Ping Pong Spel'
wn.bgcolor('red') # Spelet får bakgrundsfärgen röd
wn.setup(width=800,height=600) # Sätter storleken på fönstret till 800x600 px (pixlar)
wn.tracer(0) # Gör så att spelet inte uppdateras automatiskt

paddle_a = turtle.Turtle() # Skapar en ny variabel som jag har döpt till paddle_a. Variabeln skapar en ny turtle, detta för att skapa den vänstra paddeln i spelet.
paddle_a.speed(0) # Sätter paddel a's hastighet till den snabbaste som är möjligt
paddle_a.shape('square') # Sätter paddel a's form till en kvadrat
paddle_a.shapesize(stretch_wid=5,stretch_len=1) # Gör paddel 'a' avlång och smal. Detta för att jag använde en kvadrat som shape.
paddle_a.color('white') # Sätter färgen på paddel a till vit
paddle_a.penup() # Lyfter pennan för att undvika att rita när den flyttas
paddle_a.goto(-350,0)  # Flyttar paddel a till positionen (-350, 0) för att placera den på vänstra sidan av spelet

paddle_b = turtle.Turtle() # Skapar en ny variabel som jag har döpt till paddle_b. Variabeln skapar en ny turtle, detta för att skapa den högra paddeln i spelet.
paddle_b.speed(0) # Sätter paddel b's hastighet till den snabbaste som är möjligt
paddle_b.shape('square') # Sätter paddel b's form till en kvadrat
paddle_b.shapesize(stretch_wid=5,stretch_len=1) # Gör paddel 'b' avlång och smal. Detta för att jag använde en kvadrat som shape.
paddle_b.color('white') # Sätter färgen på paddel b till vit
paddle_b.penup() # Lyfter pennan för att undvika att rita när den flyttas
paddle_b.goto(350,0) # Flyttar paddel b till positionen (350, 0) för att placera den på högra sidan av spelet

ball = turtle.Turtle() # Skapar en ny variabel som jag har döpt till ball. Variabeln skapar en ny turtle, detta för att jag ska kunna skapa bollen i spelet.
ball.speed(0) # Sätter bollens hastighet till den snabbaste som är möjligt
ball.shape('square') # Sätter bollens form till en kvadrat
ball.color('black') # Sätter färgen på bollen till svart
ball.penup() # Lyfter pennan för att undvika att rita när den flyttas
ball.goto(0,0) # Flyttar bollen till positionen (0, 0) för att placera den i mitten av spelet
ball.dx = 0.2 # Sätter bollens rörelse i x axeln till 0.2 pixlar/uppdatering
ball.dy = 0.2 # Sätter bollens rörelse i y axeln till 0.2 pixlar/uppdatering

score_a = 0 # Skapar en variabel (score_a) som håller koll på poängen för paddle a. Variabelns start value är 0
score_b = 0 # Skapar en variabel (score_b) som håller koll på poängen för paddle b. Variabelns start value är 0

pen = turtle.Turtle() # Skapar en ny variabel som jag har döpt till pen. Variabeln skapar en ny turtle, detta för att jag ska kunna skriva ut poängen i spelet.
pen.speed(0) # Sätter pennans hastighet till den snabbaste som är möjligt
pen.penup() # Lyfter pennan för att undvika att rita när den flyttas
pen.color('white') # Sätter färgen på pennan till vit
pen.hideturtle() # Gömmer själva 'turtle' ikonen så att den inte syns i fönstret
pen.goto(0,260) # Flyttar pennan till positionen (0, 260) för att placera poängen högst upp i fönstret
pen.write('Player A: 0 Player B: 0', align='center', font=('Courier',24,'normal')) # Skriver ut texten 'Player A: 0 Player B: 0'. Texten placeras i mitten av fönstret

def paddle_a_up(): # Skapar en funktion som flyttar paddel a uppåt. Har valt att döpa funktionen till paddle_a_up
    y = paddle_a.ycor() # Hämtar den nuvarande y kordinaten för paddel a och sparar den i variabeln y
    if y < 250: # Kollar om paddel a's y kordinat är mindre än 250. Detta för att undvika att paddeln åker utanför fönstret
        y += 20 # Om paddel a's y kordinat är mindre än 250, läggs 20 pixlar till y kordinaten.
        paddle_a.sety(y) # Sätter paddel a's y kordinat till den nya y kordinaten
    
def paddle_a_down(): # Skapar en funktion som flyttar paddel a neråt. Har valt att döpa funktionen till paddle_a_down
    y = paddle_a.ycor() # Hämtar den nuvarande y kordinaten för paddel a och sparar den i variabeln y
    if y > -250: # Kollar om paddel a's y kordinat är större än -250. Detta för att undvika att paddeln åker utanför fönstret
        y -= 20 # Om paddel a's y kordinat är större än -250, dras 20 pixlar från y kordinaten.
        paddle_a.sety(y) # Sätter paddel a's y kordinat till den nya y kordinaten
    
def paddle_b_up(): # Skapar en funktion som flyttar paddel b uppåt. Har valt att döpa funktionen till paddle_b_up
    y = paddle_b.ycor() # Hämtar den nuvarande y kordinaten för paddel b och sparar den i variabeln y
    if y < 250: # Kollar om paddel b's y kordinat är mindre än 250. Detta för att undvika att paddeln åker utanför fönstret
        y += 20 # Om paddel b's y kordinat är mindre än 250, läggs 20 pixlar till y kordinaten.
        paddle_b.sety(y) # Sätter paddel b's y kordinat till den nya y kordinaten
    
def paddle_b_down(): # Skapar en funktion som flyttar paddel b neråt. Har valt att döpa funktionen till paddle_b_down
    y = paddle_b.ycor() # Hämtar den nuvarande y kordinaten för paddel b och sparar den i variabeln y
    if y > -250: # Kollar om paddel b's y kordinat är större än -250. Detta för att undvika att paddeln åker utanför fönstret
        y -= 20 # Om paddel b's y kordinat är större än -250, dras 20 pixlar från y kordinaten.
        paddle_b.sety(y) # Sätter paddel b's y kordinat till den nya y kordinaten
    
wn.listen() # Gör så att fönstret kan lyssna på tangenttryckningar
wn.onkeypress(paddle_a_up,'w') # När 'w' tangenten trycks ner, anropas funktionen paddle_a_up
wn.onkeypress(paddle_a_down,'s') # När 's' tangenten trycks ner, anropas funktionen paddle_a_down
wn.onkeypress(paddle_b_up,'Up') # När 'Up' tangenten (pilen uppåt) trycks ner, anropas funktionen paddle_b_up
wn.onkeypress(paddle_b_down,'Down') # När 'Down' tangenten (pilen neråt) trycks ner, anropas funktionen paddle_b_down

while True: # Skapar en loop som loopas igenom hela tiden för att uppdatera spelet
    wn.update() # Uppdaterar fönstret varje gång loopen loopas igenom
    
    ball.setx(ball.xcor()+ball.dx) # Flyttar bollen i x axeln med den hastighet som jag angav i ball.dx raden (variabeln)
    ball.sety(ball.ycor()+ball.dy) # Flyttar bollen i y axeln med den hastighet som jag angav i ball.dy raden (variabeln)
    
    if ball.ycor() > 290: # Kollar om bollen har åkt utanför fönstret på y axeln (där uppe)
        ball.sety(290) # Sätter bollen's y kordinat till 290 för att undvika att bollen åker utanför fönstret
        ball.dy *= -1 # Vänder på bollens rörelse i y axeln genom att multiplicera det med -1
        
    if ball.ycor() < -290: # Kollar om bollen har åkt utanför fönstret på y axeln (där nere)
        ball.sety(-290) # Sätter bollen's y kordinat till -290 för att undvika att bollen åker utanför fönstret
        ball.dy *= -1 # Vänder på bollens rörelse i y axeln genom att multiplicera det med -1
        
    if ball.xcor() > 390: # Kollar om bollen har åkt utanför fönstret på x axeln (på höger sida)
        ball.goto(0,0) # Sätter bollen's position till (0, 0) för att placera den i mitten av fönstret
        ball.dx *= -1 # Vänder på bollens rörelse i x axeln genom att multiplicera det med -1
        score_a += 1 # Lägger till 1 poäng till paddle a's poäng
        pen.clear() # Rensar den tidigare texten som visade poängen
        pen.write('Player A: {} Player B: {}'.format(score_a,score_b), align='center', font=('Courier',24,'normal')) # Skriver ut den nya poängen för paddle a och paddle b dynamiskt
        
    if ball.xcor() < -390: # Kollar om bollen har åkt utanför fönstret på x axeln (på vänster sida)
        ball.goto(0,0) # Sätter bollen's position till (0, 0) för att placera den i mitten av fönstret
        ball.dx *= -1 # Vänder på bollens rörelse i x axeln genom att multiplicera det med -1
        score_b += 1 # Lägger till 1 poäng till paddle b's poäng
        pen.clear() # Rensar den tidigare texten som visade poängen
        pen.write('Player A: {} Player B: {}'.format(score_a,score_b), align='center', font=('Courier',24,'normal')) # Skriver ut de nya poängen för paddle a och paddle b dynamiskt
        
    if -350 < ball.xcor() < -340 and (paddle_a.ycor()-50 < ball.ycor() < paddle_a.ycor()+50): # Kollar om bollen är inom paddel a's x kordinater och y kordinater
        ball.setx(-340) # Sätter bollen's x kordinat till -340 för att undvika att bollen åker in i paddeln
        ball.dx *= -1 # Vänder på bollens rörelse i x axeln genom att multiplicera det med -1
        
    if 340 < ball.xcor() < 350 and (paddle_b.ycor()-50 < ball.ycor() < paddle_b.ycor()+50): # Kollar om bollen är inom paddel b's x kordinater och y kordinater
        ball.setx(340) # Sätter bollen's x kordinat till 340 för att undvika att bollen åker in i paddeln
        ball.dx *= -1 # Vänder på bollens rörelse i x axeln genom att multiplicera det med -1