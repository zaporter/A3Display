from imageControl import *
import requests
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

def displayTemp(wait_ms=1000):
    print("Displaying temperature")
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=4956184&appid=7aefbf3a27b1650bbbb45d234b0f936f')
    temp = r.json()['main']['temp']
    temp = (temp - 273.15) * 9/5 + 32
    tempStr = '{1:.0f}F'.format(temp)
    weather = r.json()['weather']['main']

    fgColor = (230,100,120)

    img = Image.new('RGB', (LED_COLS, LED_ROWS), (0,0,0))
    font = ImageFont.truetype("fonts/helvetica.ttf", 9)
    drawText(img, temp, font, fgColor, loc=(1, 2))
    pushImage(img)
    sleep_ms(wait_ms)

