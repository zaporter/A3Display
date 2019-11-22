#!/usr/bin/env python3
# Stodd A3 display control manager
# Author: Zachary Porter

from PIL import Image, ImageFont, ImageDraw
import math
import time
from neopixel import *
import argparse
import basicDisp
import animations
import imageControl

def runDisplay(strip, filename):
    f = open(filename, "r")
    command = f.read();
    exec(command)

if __name__ == '__main__':
    print("Starting!")
    run = True
    parser = argparse.ArgumentParser()
    parser.add_argument("-h","--help", help="print help")
    parser.add_argument("-r","--run", help="run code")
    parser.add_argument("-p","--prev", help="preview")
    parser.add_argument("-f","--file", type=str, help="code file")
    parser.parse_args()
    if (parser.run):
        print("Running")
        run = True
    elif (parser.prev):
        print("Previewing")
        run = False
    else:
        print("No mode set. Assuming run")
        run = True
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    if (parser.file):
        runDisplay(strip, parser.file)
    else:
        print("No file passed. Please use -f")
    print("ending")


