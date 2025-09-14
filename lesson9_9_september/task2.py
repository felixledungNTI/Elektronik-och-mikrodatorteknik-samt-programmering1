import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.shape('turtle') # Sätter sköldpaddans form till en turtle
t.pensize(5) # Sätter storleken på penseln till 5px

t.goto(-0,-0) # Förflyttar sköldpaddan till en viss position
t.dot(20) # Sätter en punkt i sköldpaddans position
t.circle(150, 240) # Skapar en cirkel med radien 150 och antal grader den ska ritas till 240 grader
t.dot(20) # Sätter en punkt i sköldpaddans position
t.circle(150, 125) # Skapar en cirkel med radien 150 och antal grader den ska ritas till 125 grader

turtle.done()