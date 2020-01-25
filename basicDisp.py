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
GAME_FILE      = "/home/pi/commandqueue.txt"

stripColorMap=[[(0,0,0)]*LED_ROWS]*LED_COLS

strip= type('strip', (object,), {})()

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
    strip.previewImg.putpixel((x,y), colorTuple)
    if (not strip.previewMode):
        color = Color(colorTuple[0], colorTuple[1], colorTuple[2])
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
            pixel = LED_ZERO - 2 - LED_ROWS*(x-2) - 1 -y
        strip.s.setPixelColor(pixel, color)
    return True

def getPX(x,y):
    return strip.previewImg.getpixel((x,y))


def wipe(color):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX( x,y,color)
    push()
