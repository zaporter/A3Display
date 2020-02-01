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

l_score = 0
r_score = 0

def endGame():
    print("END")
    #displayText("Game Over", (255,255,255),(100,30,30),20)
    #while (not (game_popCommand() == KEY_TRIGGER)):
    #    sleep_ms(100)
    startPong()

def l_win():
    print("Left wins")
    displayText("Player 1 Wins!", (255,255,255),(30,100,30),20)
    endGame()

def r_win():
    print("Right wins")
    displayText("Player 2 Wins!", (255,255,255),(30,100,30),20)
    endGame()


def startPong():
    print("Starting game")
    ball_vx = 1
    ball_vy = 1
    
    ball = [LED_COLS/2, LED_ROWS/2]
    l_paddle = [0, LED_ROWS/2]
    r_paddle = [LED_COLS, LED_ROWS]

    print("Checking for win")
    print("Left: " + l_score)
    print("Right: " + r_score)
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
        if (ball[1] > LED_ROWS):
            ball_vy = 1
        elif (ball[1] < 0):
            ball_vy = -1

        # Check for ball falling of walls
        if (ball[0] > LED_COLS):
            l_score += 1
            startPong()
        elif (ball[0] < 0):
            r_score += 1
            startPong()

        # Update ball
        ball[0] += ball_vx
        ball[1] += ball_vy

        # Move player 1 paddle
        l_paddle_command = game_popCommand('/home/pi/A3Disp/www/html/controller_in.txt')
        if (l_paddle_command == KEY_UP):
            l_paddle[0] -= 1
        elif (l_paddle_command == KEY_DOWN):
            l_paddle[0] += 1
         
        # Move player 2 paddle
        r_paddle_command = game_popCommand('/home/pi/A3Disp/www/html/controller2_in.txt')
        if (r_paddle_command == KEY_UP):
            r_paddle[0] -= 1
        elif (r_paddle_command == KEY_DOWN):
            r_paddle[0] += 1

        # Draw Ball
        setPX(ball[0], ball[1], (200, 200, 200))

        # Draw left paddle
        for i in range(3):
            offset = i - 1
            setPX(l_paddle[0], l_paddle[1] + offset, (200, 200, 200))

        # Draw right paddle
        for i in range(3):
            offset = i - 1
            setPX(r_paddle[0], r_paddle[1] + offset, (200, 200, 200))
             
        sleep_ms(250)
        wipe((0, 0, 0))
