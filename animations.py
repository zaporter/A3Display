
from basicDisp import *
from a3time import *
import math
from neopixel import *

def anim_slowWipe(strip, color, wait_ms):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX(strip,x,y,color)
            push(strip)
            sleep_ms(wait_ms)

def anim_biFlash(strip, color1, color2, numLoops, wait_ms):
    for i in range(numLoops):
        for x in range(LED_COLS):
            for y in range(LED_ROWS):
                if ((x+y+i)%2==0):
                    setPX(strip,x,y,color1)
                else:
                    setPX(strip,x,y,color2)
        push(strip)
        sleep_ms(wait_ms)

def anim_pulseInterp(strip, color1, color2, numLoops, loopTime):
    pos = 0
    pi=3.1415
    pos2 = pi/2.0
    numSteps=1000.0
    numSteps1=1000
    diff = pi/numSteps
    for i in range(numLoops):
        for j in range (numSteps1):
            col1 = ((color1[0]*math.cos(pos), color1[1]*math.cos(pos + 2), color1[2]*math.cos(pos - 2)))
            col2 = ((color2[0]*math.cos(pos2), color2[1]*math.cos(pos2 + 2), color2[2]*math.cos(pos2 - 2)))
            #print("-")
            #print(col1)
            #print(col2)
            ccol = Color(abs(int(col1[0])), abs(int(col1[1])), abs(int(col1[2])))
            ccol2 = Color(abs(int(col2[0])), abs(int(col2[1])), abs(int(col2[2])))
            combinedColor = int(ccol+ccol2)
            #print (combinedColor)
            wipe(strip, combinedColor)
            pos+=diff
            pos2+=diff
            sleep_ms(loopTime)

def anim_pulse(strip, color, numLoops, loopTime):
    anim_pulseInterp(strip, (0,0,0), color,numLoops, loopTime)
