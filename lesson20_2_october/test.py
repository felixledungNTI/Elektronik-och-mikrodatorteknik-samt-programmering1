import turtle
import time
import random

# --- Konstanter ---
DELAY = 0.1
MOVE_STEP = 20
SCREEN_SIZE = 600
FOOD_INTERVAL = 10  # sekunder

# --- Variabler ---
score = 0
highScore = 0
segments = []
last_food_time = time.time()

# --- Skärm ---
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
wn.tracer(0)

# --- Ormens huvud ---
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# --- Mat ---
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

# --- Poängvisning ---
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, SCREEN_SIZE//2 - 40)
scoreBoard.write(f'Score: {score} High Score: {highScore}',
                 align='center', font=('Arial', 24, 'normal'))

# --- Game Over ---
gameOver = turtle.Turtle()
gameOver.speed(0)
gameOver.color('red')
gameOver.penup()
gameOver.hideturtle()

# --- Funktioner ---
def update_score():
    scoreBoard.clear()
    scoreBoard.write(f'Score: {score} High Score: {highScore}',
                     align='center', font=('Arial', 24, 'normal'))

def reset_game():
    global score, segments, DELAY
    head.goto(0, 0)
    head.direction = 'stop'
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()
    score = 0
    DELAY = 0.1
    update_score()

def move_head():
    x, y = head.xcor(), head.ycor()
    if head.direction == 'up': head.sety(y + MOVE_STEP)
    elif head.direction == 'down': head.sety(y - MOVE_STEP)
    elif head.direction == 'left': head.setx(x - MOVE_STEP)
    elif head.direction == 'right': head.setx(x + MOVE_STEP)

def spawn_food():
    x = random.randint(-SCREEN_SIZE//2//MOVE_STEP + 1, SCREEN_SIZE//2//MOVE_STEP - 1) * MOVE_STEP
    y = random.randint(-SCREEN_SIZE//2//MOVE_STEP + 1, SCREEN_SIZE//2//MOVE_STEP - 1) * MOVE_STEP
    food.goto(x, y)

# --- Styrning ---
def go_up():    head.direction = 'up' if head.direction != 'down' else head.direction
def go_down():  head.direction = 'down' if head.direction != 'up' else head.direction
def go_left():  head.direction = 'left' if head.direction != 'right' else head.direction
def go_right(): head.direction = 'right' if head.direction != 'left' else head.direction

wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# --- Huvudloop ---
while True:
    wn.update()
    
    # Mat spawnar automatiskt varje FOOD_INTERVAL sekunder
    if time.time() - last_food_time > FOOD_INTERVAL:
        spawn_food()
        last_food_time = time.time()
    
    move_head()
    
    # Kollision med vägg
    if abs(head.xcor()) > SCREEN_SIZE//2 - MOVE_STEP or abs(head.ycor()) > SCREEN_SIZE//2 - MOVE_STEP:
        gameOver.goto(0, 0)
        gameOver.write("Game Over", align='center', font=('Arial', 24, 'normal'))
        wn.update()
        time.sleep(2)
        gameOver.clear()
        reset_game()
    
    # Kollision med mat
    if head.distance(food) < MOVE_STEP:
        spawn_food()
        last_food_time = time.time()
        newSeg = turtle.Turtle()
        newSeg.speed(0)
        newSeg.shape('square')
        newSeg.color('green')
        newSeg.penup()
        segments.append(newSeg)
        score += 10
        if score > highScore:
            highScore = score
        update_score()
    
    # Flytta ormens segment
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    
    # Kollision med egen kropp
    for seg in segments:
        if head.distance(seg) < MOVE_STEP:
            time.sleep(1)
            reset_game()
            break
    
    time.sleep(DELAY)