from imageControl import *
import datetime

def displayTime(strip, wait_ms):
    print("Displaying time")
    timestr = '{date:%H:%M}'.format(date=datetime.datetime.now())
    img = Image.new('RGB',(LED_COLS, LED_ROWS), (0,0,0))
    font = ImageFont.truetype("fonts/helvetica.ttf", 9)
    drawText(strip,img,timestr,font,(200,200,0),loc=(1,2))
    pushImage(strip,img)
    sleep_ms(strip,wait_ms)
