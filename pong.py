from gameFeed import *
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
    startPong()

def winGame():
    displayText("You won!", (255,255,255),(30,100,30),20)

def startPong():
    print("started")
    ball_vx = 1
    ball_vy = 
    
    ball = 
