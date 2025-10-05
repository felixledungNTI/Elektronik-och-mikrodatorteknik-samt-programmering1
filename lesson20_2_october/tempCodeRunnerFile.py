import turtle
import time
import random

delay = 0.1

score = 0

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

segments = []

scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape('square')
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write('Score: 0',
                 align='center',
                 font=('Arial', 24, 'normal'))
wn.update()

gameOver = turtle.Turtle()
gameOver.speed(0)
gameOver.color('red')
gameOver.penup()
gameOver.hideturtle()


def up():
    if head.direction != 'down':
        head.direction = 'up'


def down():
    if head.direction != 'up':
        head.direction = 'down'


def left():
    if head.direction != 'right':
        head.direction = 'left'


def right():
    if head.direction != 'left':
        head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkey(up, 'w')
wn.onkey(down, 's')
wn.onkey(left, 'a')
wn.onkey(right, 'd')

food_timer = time.time()


def updateScore():
    scoreBoard.clear()
    scoreBoard.write('Score: {}'.format(score),
        align='center',
        font=('Arial', 24, 'normal'))

while True:
    if time.time() - food_timer > 10:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)
        food_timer = time.time()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor(
    ) > 290 or head.ycor() < -290:
        gameOver.goto(0, 0)
        gameOver.write('Game Over',
                       align='center',
                       font=('Arial', 24, 'normal'))
        time.sleep(2)
        gameOver.clear()

        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        updateScore()

        delay = 0.1


    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x,y)
        food_timer = time.time()
        
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape('square')
        newSegment.color('green')
        newSegment.penup()
        newSegment.goto(head.xcor(), head.ycor())
        segments.append(newSegment)

        score += 2
        updateScore()

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            updateScore()

            delay = 0.1

    move()
    wn.update()
    time.sleep(delay)
wn.mainloop()
