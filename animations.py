#Super simple animations
#Author: Zack Porter

from basicDisp import *
from a3time import *
import math
import random

try:
    from neopixel import *
except ImportError:
    pass


def anim_slowWipe(color, wait_ms):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX(x,y,color)
            push()
            sleep_ms(wait_ms)

def anim_biFlash( color1, color2, numLoops, wait_ms):
    for i in range(numLoops):
        for x in range(LED_COLS):
            for y in range(LED_ROWS):
                if ((x+y+i)%2==0):
                    setPX(x,y,color1)
                else:
                    setPX(x,y,color2)
        push()
        sleep_ms(wait_ms)

def anim_pulseInterp( color1, color2, numLoops, loopTime):
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
            combinedColor = col1+col2
            #print (combinedColor)
            wipe( combinedColor)
            pos+=diff
            pos2+=diff
            sleep_ms(loopTime)

def anim_pulse( color, numLoops, loopTime):
    anim_pulseInterp( (0,0,0), color,numLoops, loopTime)

def anim_stepFade(percent):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            col = getPX(x,y)
            col2= (int(col[0] * (1.0-percent)),int( col[1]*(1.0-percent)),int( col[2]*(1.0-percent)))
            #print(str(col)+">"+str(col2))
            setPX(x,y,col2)
    push()

def anim_rColorWalk(numSteps, wait=50,maxC=200,fade=0.02):
    xpos=LED_COLS/2
    ypos=LED_ROWS/2
    lc=0
    while (lc<numSteps):
        lc+=1
        xvel=0
        yvel=0
        while (xvel==0 and yvel==0):
            xvel=random.randrange(-2,2)
            yvel=random.randrange(-2,2)
        cr=random.randrange(0,maxC)
        cg=random.randrange(0,maxC)
        cb=random.randrange(0,maxC)
        while (setPX(xpos+xvel, ypos+yvel,(cr,cg,cb))):
            xpos+=xvel
            ypos+=yvel
            anim_stepFade(fade)
            sleep_ms(wait)

def anim_flashFade(color, wait_ms, fade=0.1):
    wipe(color)
    for x in range (int(5.0/fade)):
        anim_stepFade(fade)
        sleep_ms(wait_ms)

def anim_rain(color, count, numDrops, wait_ms, fade=0.1):
    spots=[0]*numDrops
    for x in range(count):
        for k in range(numDrops):
            if not (spots[k] == 0):
                spots[k][1]+=1
                if not (setPX(spots[k][0],spots[k][1],color)):
                    spots[k]=0
            else:
                if (random.randrange(0,numDrops)==1):
                    spots[k]=[random.randrange(0,LED_COLS), -1]
        anim_stepFade(fade)
        sleep_ms(wait_ms)

    



