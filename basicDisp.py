LED_ROWS       = 12
LED_COLS       = 25
LED_COUNT      = LED_ROWS*LED_COLS
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 255
LED_INVERT     = False
LED_CHANNEL    = 0
LED_ZERO = 278

def push(strip):
    strip.show()
# Color is Color(R,G,B)
def setPX(strip, x, y, color):
    if (x>=LED_COLS or x<0 or y>=LED_ROWS or y<0):
        print('Invalid set. Outside of bounds')
    else:
        pixel = 0
        if (x==0):
            pixel = LED_ZERO+y
        elif (x==1):
            if (y==0 or y==1):
                pixel = LED_ZERO - (2-y)
            else:
                pixel = LED_ZERO + 23 - y
        elif (x%2==0 and x<=5):
            pixel = LED_ZERO - 3 -LED_ROWS*(x-2)- y
        elif (x%2==0 and x>5):
            pixel = LED_ZERO - 2 -LED_ROWS*(x-1)+y
        elif (x%2==1 and x<6):
            pixel = LED_ZERO - 3 - LED_ROWS*(x-1)+1 + y
        elif (x%2==1 and x>5):
            pixel = LED_ZERO - 2 -LED_ROWS*(x-2)-1 -y
        strip.setPixelColor(pixel, color)

def wipe(strip, color):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX(strip, x,y,color)
    push(strip)
