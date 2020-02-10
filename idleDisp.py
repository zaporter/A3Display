from imageControl import *
import datetime
import math

def displayTime(wait_ms=1000):
    print("Displaying time")
    timestr = '{date:%H:%M}'.format(date=datetime.datetime.now())
    minute = datetime.datetime.now().minute
    pos = (minute/30.0) * 3.14159
    topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
    topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
    img = Image.new('RGB',(LED_COLS, LED_ROWS), (0,0,0))
    font = ImageFont.truetype("fonts/helvetica.ttf", 9)
    drawText(img,timestr,font,topColor,loc=(1,2))
    pushImage(img)
    sleep_ms(wait_ms)


