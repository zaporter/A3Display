#!/usr/bin/env python3
# Stodd A3 display control manager
# Author: Zachary Porter, Jake Roller

from PIL import Image, ImageFont, ImageDraw
import math
import time
from neopixel import *
import argparse
import basicDisp
import animations
import imageControl

def runDisplay(strip):
    f = open("demos/scrollText.py", "r")
    command = f.read();
    exec(command)

if __name__ == '__main__':
    print("Starting!")
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    runDisplay(strip)
    #image = Image.new('RGB',(25,12),color=(0,0,0))
    #scrollText(strip,image,"A3 DISPLAY",font2,(255,0,0,255),50,200,loc=(0,-1))
    """
  
	#image = Image.new('RGB',(25,12),color=(0,0,20))
	#scrollText(strip, image, "RIP", font, (255,150,0,255), 100, 10)
	
        pos+=0.1
        topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
        topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
        image = Image.new('RGB',(25,12),color=(0,0,20))
        drawText(strip, image, "RIP", font, (255,150,0,255),loc=(3,-1))
        drawBorder(image,topColor)
        pushImage(strip,image)
        time.sleep(1)
        pos+=0.1
        topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
        topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
        image = Image.new('RGB',(25,12),color=(0,0,20))
        drawText(strip, image, "Larry", font2, (155,250,0,255),loc=(1,-1))
        drawBorder(image,topColor)
        pushImage(strip,image)
        time.sleep(1)
	
	draw
    """
    """
    #anim_pulseInterp(strip,Color(255,0,0),Color(0,0,255),1,10000)
           # setPX(strip,x,y,Color(255*x/LED_COLS,255*y/LED_ROWS,90-90*(x/LED_COLS)))
    push(strip)
    time.sleep(15)
    #anim_pulse(strip,Color(255,255,255),10,100)
    wipe(strip,Color(0,0,0))
    """
    print("ending")


