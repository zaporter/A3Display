from gameFeed import *
from basicDisp import *
from a3time import *
from imageControl import *
import math
import random

#Gameboy commands
#"U" -- Up pad
#"D" -- Down pad
#"L" -- Left pad
#"R" -- Right pad
#"T" -- Trigger

KEY_UP="U"
KEY_DOWN="D"
KEY_LEFT="L"
KEY_RIGHT="R"
KEY_TRIGGER="T"

def endGame(score):
    print("END")
    
    for x in range(3):
        wipe((50,10,10))
        sleep_ms(200)
        wipe((30,30,30))
        sleep_ms(200)
    displayText("Score: "+str(score), (100,10,10),(20,30,30),20,loops=1)
    sleep_ms(500)
   
    #while (not (game_popCommand() == KEY_TRIGGER)):
    #    sleep_ms(100)
    startSnake()

def winGame():
    displayText("You won!", (255,255,255),(30,100,30),20)

def l_win():
    print("Left wins")
    displayText("Player 1 Wins!", (255,255,255),(30,100,30),20)
    startPong()

def r_win():
    print("Right wins")
    displayText("Player 2 Wins!", (255,255,255),(30,100,30),20)
    startPong()

def startPong():
    # Start game with l_score, r_score, and paddle_size
    pongGame(0, 0, 3, 1)

def pongGame(l_score, r_score, paddle_size, speed):
    print("Starting game")
    seed = random.randint(1, 4)
    if (seed == 1):
        ball_vx = 1
        ball_vy = 1
    elif (seed == 2):
        ball_vx = 1
        ball_vy = -1
    elif (seed == 3):
        ball_vx = -1
        ball_vy = 1
    else:
        ball_vx = -1
        ball_vy = -1
    
    ball = [LED_COLS/2, LED_ROWS/2]
    l_paddle = [0, LED_ROWS/2]
    r_paddle = [LED_COLS-1, LED_ROWS/2]

    print("Checking for win")
    print("Left: " + str(l_score))
    print("Right: " + str(r_score))
    if (l_score > 10):
        l_score = 0
        r_score = 0
        l_win()
    elif (r_score > 10):
        l_score = 0
        r_score = 0
        r_win()
    while True:
        
        # Check for ball bounce on ceiling and floor
        if (ball[1] > LED_ROWS - 2):
            ball_vy = -1 * abs(ball_vy)
        elif (ball[1] < 1):
            ball_vy = abs(ball_vy)

        # Check for ball falling of walls
        if (ball[0] > LED_COLS):
            l_score += 1
            pongGame(l_score, r_score, paddle_size, speed + 1)
        elif (ball[0] < 0):
            r_score += 1
            pongGame(l_score, r_score, paddle_size, speed + 1)

        # Check for ball bouncing on paddle
        if (ball[0] == LED_COLS - 2 and ball[1] >= l_paddle[1] - paddle_size // 2 and ball[1] <= l_paddle[1] + paddle_size // 2):
            ball_vx = -1 * abs(ball_vx)
        elif (ball[0] == 1 and ball[1] >= r_paddle[1] - paddle_size // 2 and ball[1] <= r_paddle[1] + paddle_size // 2):
            ball_vx = abs(ball_vx) 

        # Update ball
        ball[0] += ball_vx
        ball[1] += ball_vy

        # Move player 1 paddle
        l_paddle_command = game_popCommand(GAME_INPUT1)
        if (l_paddle_command == KEY_UP and l_paddle[1] - 1 > 0):
            l_paddle[1] -= 1
        elif (l_paddle_command == KEY_DOWN and l_paddle[1] + 1 < LED_ROWS):
            l_paddle[1] += 1
         
        # Move player 2 paddle
        r_paddle_command = game_popCommand(GAME_INPUT2)
        if (r_paddle_command == KEY_UP and r_paddle[1] - 1 > 0):
            r_paddle[1] -= 1
        elif (r_paddle_command == KEY_DOWN and r_paddle[1] + 1 < LED_ROWS):
            r_paddle[1] += 1

        # Draw Ball
        color_r = random.randint(10, 200)
        color_g = random.randint(10, 200)
        color_b = random.randint(10, 200)
        setPX(ball[0], ball[1], (color_r, color_g, color_b))

        # Draw left paddle
        for i in range(paddle_size):
            offset = i - paddle_size // 2 
            setPX(l_paddle[0], l_paddle[1] + offset, (200, 200, 200))

        # Draw right paddle
        for i in range(paddle_size):
            offset = i - paddle_size // 2 
            setPX(r_paddle[0], r_paddle[1] + offset, (200, 200, 200))

        push() 
        sleep_ms(speed * 10 / 1000)
        wipe((0, 0, 0), clear = False)

def startSnake():
    print("started")
    game_clear(GAME_INPUT1)
    wipe((0,0,0))
    xvel=1
    yvel=0
    candyX=5
    candyY=5
    snake=[[LED_COLS/2, LED_ROWS/2],[0,0]]
    while True:
        command=game_popCommand(GAME_INPUT1)
        if (command==KEY_UP and yvel!=1):
            xvel=0
            yvel=-1
        elif (command==KEY_DOWN and yvel!=-1):
            xvel=0
            yvel=1
        elif(command==KEY_RIGHT and xvel!=-1):
            xvel=1
            yvel=0
        elif(command==KEY_LEFT and xvel!=1):
            xvel=-1
            yvel=0
        setPX(snake[len(snake)-1][0],snake[len(snake)-1][1],(0,0,0))
        snake[0][0]+=xvel
        snake[0][1]+=yvel
        #snake.append([1,1])
        if (snake[0][0]==candyX and snake[0][1]==candyY):
            snake.append([-1,-1])
            print("SNAKE LEN: "+str(len(snake)))
            candyX=random.randrange(1,LED_COLS-1)
            candyY=random.randrange(1,LED_ROWS-1)
        for x in range(len(snake)):
            if (snake[0][0] == snake[x][0] and snake[0][1]==snake[x][1] and x!=0):
                endGame(len(snake)-2)
        for x in range(len(snake)-1):
            snake[len(snake)-x-1]=[snake[len(snake)-x-2][0], snake[len(snake)-x-2][1]]
        for x in range(len(snake)):
            if not (setPX(snake[x][0], snake[x][1],(30*x,20*len(snake)+10*x,25*len(snake)))):
                endGame(len(snake)-2)
        setPX(candyX, candyY, (255,200,0))
        push()
        sleep_ms(100)
        


