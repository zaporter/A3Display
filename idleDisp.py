from imageControl import *
import datetime

def displayTime(wait_ms=1000):
    print("Displaying time")
    timestr = '{date:%H:%M}'.format(date=datetime.datetime.now())
    img = Image.new('RGB',(LED_COLS, LED_ROWS), (0,0,0))
    font = ImageFont.truetype("fonts/helvetica.ttf", 9)
    drawText(img,timestr,font,(200,10,10),loc=(1,2))
    pushImage(img)
    sleep_ms(wait_ms)


