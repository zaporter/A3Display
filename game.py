from gameFeed import *
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
    displayText("Game Over", (255,255,255),(100,30,30),20)

def winGame():
    displayText("You won!", (255,255,255),(30,100,30),20)

def startSnake():
    xvel=1
    yvel=0
    candyX=5
    candyY=5
    snake=[[LED_COLS/2, LED_ROWS/2]]
    while True:
        command=game_popCommand()
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
        if (snake[0]==candyX and snake[1]==candyY):
            snake.append([0,0])
            candyX=random.randrange(1,LED_COLS-1)
            candyY=random.randrange(1,LED_ROWS-1)
        for x in range(len(snake)):
            if (snake[0][0] == snake[x][0] and snake[0][1]==snake[x][1]):
                endGame()
        for x in range(len(snake)-1):
            snake[x+1][0]=snake[x][0]
            snake[x+1][1]=snake[x][1]
        wipe((0,0,0))
        for x in range(len(snake)):
            if not (setPX(snake[x][0], snake[x][1],(255,255,255))):
                endGame()
        setPX(candyX, candyY, (255,200,0))
        push()
        wait_ms(100)

        


