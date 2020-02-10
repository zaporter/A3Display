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
from idleDisp import *
from game import *

try:
    from neopixel import *
except ImportError:
    pass


def runDisplay(strip, filename_a3d):
    f_a3d = open(filename_a3d, "r")
    command_a3d = f_a3d.read();
    exec(command_a3d,globals(),locals())

if __name__ == '__main__':
    print("Starting!")
    run = True
    init_gain_map()
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--run", action="store_true", help="run code")
    parser.add_argument("-p","--prev", action="store_true", help="preview")
    parser.add_argument("-l", "--length", action="store", type=int, help="Set length of preview in seconds")
    parser.add_argument("-f","--file", action="store", type=str, help="code file")
    parser.add_argument("-o","--output", action="store", type=str, help="Location to save preview")
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
    if (run):
        strip.s = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.s.begin()
        # Holy shit.. Python is insane
        strip.previewMode=False
        strip.previewImg = Image.new('RGB', (LED_COLS, LED_ROWS), (0,0,0))
    else:
        strip.previewMode=True
        strip.previewImg = Image.new('RGB', (LED_COLS, LED_ROWS), (0,0,0))
        strip.previewFrames = []
        strip.previewLength = parser.length
        strip.previewFile = parser.output
    if(parser.file):
        runDisplay(strip, parser.file)
    else:
        print("No file passed. Please use -f")
    print("ending")

