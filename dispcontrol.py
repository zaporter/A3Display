#!/usr/bin/env python3
# Stodd A3 display control manager
# Author: Zachary Porter

from PIL import Image, ImageFont, ImageDraw
import math
import time
import argparse

from basicDisp import *
from animations import *
from imageControl import *

try:
    from neopixel import *
except ImportError:
    pass

def runDisplay(strip, filename):
    f = open(filename, "r")
    command = f.read();
    ikf = locals()
    exec(command,globals(),locals())

if __name__ == '__main__':
    print("Starting!")
    run = True
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--run", action="store_true", help="run code")
    parser.add_argument("-p","--prev", action="store_true", help="preview")
    parser.add_argument("-l", "--length", action="store", type=int, help="Set length of preview in seconds")
    parser.add_argument("-f","--file", action="store", type=str, help="code file")
    parser = parser.parse_args()
    if (parser.run):
        print("Running")
        run = True
    elif (parser.prev):
        print("Previewing")
        run = False
    else:
        print("No mode set. Assuming run")
        run = True
    # Insanity. 
    strip= type('strip', (object,), {})()
    if run:
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
        # Holy shit.. Python is insane
        strip.previewMode=False
    else:
        strip.previewMode=True
        strip.previewImg = Image.new('RGB', (LED_COLS, LED_ROWS), (0,0,0))
        strip.previewFrames = []
        strip.previewLength = parser.length
    if(parser.file):
        runDisplay(strip, parser.file)
    else:
        print("No file passed. Please use -f")
    print("ending")

