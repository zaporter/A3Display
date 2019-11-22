#!/usr/bin/env python3
# Stodd A3 display control manager
# Author: Zachary Porter, Jake Roller

from PIL import Image, ImageFont, ImageDraw
import math
import time
from neopixel import *
import argparse
from basicDisp import *
from animations import *
from imageControl import *

def runDisplay(strip):
    f = open("demos/scrollText.py", "r")
    command = f.read();
    ikf = locals()
    exec(command,globals(),locals())

if __name__ == '__main__':
    print("Starting!")
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    setPX(strip,5,5,Color(255,255,255))
    push(strip)
    runDisplay(strip)
    #image = Image.new('RGB',(25,12),color=(0,0,0))
    #scrollText(strip,image,"A3 DISPLAY",font2,(255,0,0,255),50,200,loc=(0,-1))


