import turtle

# Skapa skärm
screen = turtle.Screen()
screen.title("Blå, Vit, Gul Flagga")
screen.bgcolor("white")

# Skapa sköldpadda
t = turtle.Turtle()
t.speed(10)

def draw_rectangle(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Mått
flag_width = 300
flag_height = 180
stripe_width = flag_width // 3

# Rita flaggans fält
draw_rectangle("blue", -flag_width//2, -flag_height//2, stripe_width, flag_height)   # vänster (blå)
draw_rectangle("white", -flag_width//2 + stripe_width, -flag_height//2, stripe_width, flag_height)  # mitten (vit)
draw_rectangle("yellow", -flag_width//2 + 2*stripe_width, -flag_height//2, stripe_width, flag_height)  # höger (gul)

t.hideturtle()
screen.mainloop()