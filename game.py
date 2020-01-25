from gameFeed import *

def startSnake():
    xvel=1
    yvel=0
    candyX=5
    candyY=5
    snake=[[LED_COLS/2, LED_ROWS/2]]
    while True:
        snake[0][0]+=xvel
        snake[0][1]+=yvel
        for x in range(len(snake)-1):
            snake[x+1][0]=snake[x][0]
            snake[x+1][1]=snake[x][1]
        wipe((0,0,0))
        for x in range(len(snake)):
            setPX(snake[x][0], snake[x][1],(255,255,255))
        setPX(candyX, candyY, (255,200,0))
        push()

        


