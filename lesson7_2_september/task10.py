import turtle

s = turtle.getscreen()
t = turtle.Turtle()

s.bgcolor('skyblue')

def filled_circle(radie,color): # Skapar en cirkel med radie och färg. Radien och färgen bestäms när funktionen anropas
    t.color(color,color) # Sätter färgen på halvcirkeln, din den färg som har angetts i funktionen.
    t.begin_fill() # "Start" markerar objektet, som ska fyllas
    t.setheading(-270) # Bestäms sköldpaddans position, i detta fall till -270 grader
    t.circle(radie, 180) # Sätter cirkelns radie, utifrån den variabel som har definerats. variabelns value är radie
    t.left(90) # Roterar sköldpaddan 90 grader
    t.forward(radie*2) # Förflyttar sköldpaddans till en viss position (x, y) i detta fall x = radie*2 och y = 0
    t.end_fill() # Slutar fylla objektet med färg
    t.right(180) # Roterar sköldpaddan 180 grader
    
filled_circle(100, 'red') # Skapar en cirkel med radie 100 och färgen "röd"
filled_circle(95, 'orange') # Skapar en cirkel med radie 95 och färgen "orange"
filled_circle(90, 'yellow') # Skapar en cirkel med radie 90 och färgen "gul"
filled_circle(85, 'green') # Skapar en cirkel med radie 85 och färgen "grön"
filled_circle(80,'blue') # Skapar en cirkel med radie 80 och färgen "blå"
filled_circle(75,'purple') # Skapar en cirkel med radie 75 och färgen "lila"
filled_circle(70,'pink') # Skapar en cirkel med radie 70 och färgen "rosa"

turtle.done()