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

def endGame():
    print("END")
    #displayText("Game Over", (255,255,255),(100,30,30),20)
    #while (not (game_popCommand() == KEY_TRIGGER)):
    #    sleep_ms(100)
    startSnake()

def winGame():
    displayText("You won!", (255,255,255),(30,100,30),20)

def startSnake():
    print("started")
    xvel=1
    yvel=0
    candyX=5
    candyY=5
    snake=[[LED_COLS/2, LED_ROWS/2],[0,0]]
    while True:
        print("in")
        command=game_popCommand(GAME_FILE)
        if (command==KEY_UP):
            xvel=0
            yvel=-1
        elif (command==KEY_DOWN):
            xvel=0
            yvel=1
        elif(command==KEY_RIGHT):
            xvel=1
            yvel=0
        elif(command==KEY_LEFT):
            xvel=-1
            yvel=0
        snake[0][0]+=xvel
        snake[0][1]+=yvel
        print("df")
        #snake.append([1,1])
        if (snake[0][0]==candyX and snake[0][1]==candyY):
            snake.append([-1,-1])
            print("SNAKE LEN: "+str(len(snake)))
            candyX=random.randrange(1,LED_COLS-1)
            candyY=random.randrange(1,LED_ROWS-1)
        for x in range(len(snake)):
            if (snake[0][0] == snake[x][0] and snake[0][1]==snake[x][1] and x!=0 and y!=0):
                endGame()
        for x in range(len(snake)-1):
            snake[len(snake)-x-1]=[snake[len(snake)-x-2][0], snake[len(snake)-x-2][1]]
        for x in range(len(snake)):
            if not (setPX(snake[x][0], snake[x][1],(50*x,50*len(snake),25*len(snake)))):
                endGame()
        print("YE")
        setPX(candyX, candyY, (255,200,0))
        push()
        print("k")
        sleep_ms(250)
        wipe((0,0,0))
        print("e")
        


