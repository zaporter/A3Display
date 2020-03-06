# Basic display functionality
# Author: Zack Porter

import sys
from PIL import Image
try:
    from neopixel import *
except ImportError:
    pass

LED_ROWS       = 12
LED_COLS       = 25
LED_COUNT      = LED_ROWS*LED_COLS
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0
LED_ZERO       = 278
GAME_INPUT1    = "/home/pi/A3Display/www/html/controller_in.txt"
GAME_INPUT2    = "/home/pi/A3Display/www/html/controller2_in.txt"
LED_COLOR_GAIN = 8
LED_COLOR_CONSTANT = ((255.0/LED_COLOR_GAIN) + 1) ** (1.0/255.0) # Approx solution to A(k^255 - 1) = 255
LED_GAIN_MAP   = [0]*256
LED_MAPPING_MAP= [0] # WILL BE LED_COLS x LED_ROWS
stripColorMap  = [0] # WILL BE LED_COLS x LED_ROWS
strip= type('strip', (object,), {})()

print("Initializing basic maps")
LED_MAPPING_MAP=[0]*LED_COLS
for i in range(LED_COLS):
    LED_MAPPING_MAP[i] = [0] * LED_ROWS

stripColorMap= [0]*LED_COLS
for i in range(LED_COLS):
    stripColorMap[i] = [0] * LED_ROWS

def init_mapping_map():
    print("Initializing mapping map")
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            pixel = 0
            if (x==0):
                pixel = LED_ZERO+y
            elif (x==1):
                if (y==0 or y==1):
                    pixel = LED_ZERO - (2-y)
                else:
                    pixel = LED_ZERO + 23 - y
            elif (x%2==0 and x<=5):
                pixel = LED_ZERO - 3 - LED_ROWS*(x-2) - y
            elif (x%2==0 and x>5):
                pixel = LED_ZERO - 2 - LED_ROWS*(x-1) + y
            elif (x%2==1 and x<6):
                pixel = LED_ZERO - 3 - LED_ROWS*(x-1) + 1 + y
            elif (x%2==1 and x>5):
                pixel = LED_ZERO - 2 - LED_ROWS*(x-2) - 1 - y
            LED_MAPPING_MAP[x][y]=pixel

def init_gain_map():
    print("Initializing gain map")
    for x in range(256):
        LED_GAIN_MAP[x]=int(LED_COLOR_GAIN*((LED_COLOR_CONSTANT ** (x))-1)) 

def init_led_maps():
    init_mapping_map()
    init_gain_map()

def push():
    if (strip.previewMode):
        strip.previewFrames.append(strip.previewImg.copy())
        if (len(strip.previewFrames)/15.0 > strip.previewLength):
            strip.previewFrames[0].save(strip.previewFile, format='GIF', append_images=strip.previewFrames[1:],save_all=True, duration=67)
            sys.exit(0)
    else:
        strip.s.show()

# Color is Color(R,G,B)
def setPX(x, y, colorTuple):
    if (x>=LED_COLS or x<0 or y>=LED_ROWS or y<0):
      #  print('Invalid set. Outside of bounds')
        return False
    stripColorMap[x][y]=colorTuple
    
    if (strip.previewMode):
        strip.previewImg.putpixel((x,y), colorTuple)
    else:
        # Compute new color along exponential curve
        # color(x) = A(k^x - 1)
        # color(0) = 0
        # color(255) = 255
        color = Color(
                LED_GAIN_MAP[colorTuple[0]%256],
                LED_GAIN_MAP[colorTuple[1]%256],
                LED_GAIN_MAP[colorTuple[2]%256])
        pixel = LED_MAPPING_MAP[x][y]
        strip.s.setPixelColor(pixel, color)
    return True

def getPX(x,y):
    return stripColorMap[x][y] 

def wipe(color, clear=True):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX( x,y,color)
    if (clear):
        push()
