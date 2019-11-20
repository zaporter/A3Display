#!/usr/bin/env python3
# Stodd A3 display control manager
# Author: Zachary Porter
from PIL import Image, ImageFont, ImageDraw
import math
import time
from neopixel import *
import argparse


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

def anim_slowWipe(strip, color, wait_ms):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            setPX(strip,x,y,color)
            push(strip)
            time.sleep(wait_ms/1000.0)

def anim_biFlash(strip, color1, color2, numLoops, wait_ms):
    for i in range(numLoops):
        for x in range(LED_COLS):
            for y in range(LED_ROWS):
                if ((x+y+i)%2==0):
                    setPX(strip,x,y,color1)
                else:
                    setPX(strip,x,y,color2)
        push(strip)
        time.sleep(wait_ms/1000.0)

def anim_pulseInterp(strip, color1, color2, numLoops, loopTime):
    pi = 3.14159
    pos = 0
    pos2 = -pi/2.0
    numSteps=1000.0
    numSteps1=1000
    diff = pi/numSteps
    for i in range(numLoops):
        for j in range (numSteps1):
            print("-")
            bri1 = math.sin(pos) * math.sin(pos)
            bri2 = 1.0-(math.sin(pos) * math.sin(pos))
            print(bri1)
            print(bri2)
            col1 = bri1*color1
            col2 = bri2*color2
            print(col1)
            print(col2)
            combinedColor = int(col1+col2)
            print(combinedColor)
            wipe(strip, combinedColor)
            pos+=diff
            pos2+=diff
            time.sleep(1000.0/1000.0)

def anim_pulse(strip, color, numLoops, loopTime):
    anim_pulseInterp(strip, Color(0,0,0), color,numLoops, loopTime)

def pushImage(strip, img):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            col = img.getpixel((x,y))
            color = Color(col[0],col[1],col[2])
            setPX(strip,x,y,color)
    push(strip)

def pushImageFile(strip, filename):
    img = Image.open(filename)
    pushImage(strip,img)

def drawText(strip, img, text, font, colorRGB, loc=(0,0)):
    draw = ImageDraw.Draw(img)
    draw.text(loc,text,font=font, fill=colorRGB)

def findFirstDiff(img1, img2):
    for x in range(LED_COLS):
	for y in range(LED_ROWS):
	    if img1.getpixel((x,y))[0] != img2.getpixel((x,y))[0]:
		return (x,y)
	    if img1.getpixel((x,y))[1] != img2.getpixel((x,y))[1]:
		return (x,y)
	    if img1.getpixel((x,y))[2] != img2.getpixel((x,y))[2]:
		return (x,y)
    return (-1,-1)

def isEquivImg(img1, img2):
    return (findFirstDiff(img1,img2) == (-1,-1))

def scrollText(strip, img, text, font, colorRGB, wait_ms, scroll_no, loc=(0,0)):
    back_img = img.copy()
    draw = ImageDraw.Draw(img)
    draw.text(loc,text,font=font,fill=colorRGB)
    size= draw.textsize(text,font)
    print("text width: ",size[0])
    for i in range(scroll_no):
	#scroll_loc=(size[0]-25,loc[1])
	scroll_loc=(LED_COLS,loc[1])
	for x in range(size[0]+LED_COLS):
	    """
	    draw.text(scroll_loc,text,font=font,fill=colorRGB)
	    scroll_loc=(scroll_loc[0]-1,scroll_loc[1])
	    pushImage(strip,img)
	    img = back_img.copy()
	    draw = ImageDraw.Draw(img)
	    time.sleep(wait_ms/1000.0)
	    """
	    #print(scroll_loc)
	    draw.text(scroll_loc,text,font=font,fill=colorRGB)
	    scroll_loc=(scroll_loc[0]-1,scroll_loc[1])
	    pushImage(strip,img)
	    img = back_img.copy()
	    draw = ImageDraw.Draw(img)
	    time.sleep(wait_ms/1000.0)
    """
    while not isEquivImg(back_img,img):
	draw.text(start_loc,text,font=font,fill=colorRGB)
	start_loc=(start_loc[0]-1,start_loc[1])
	img = back_img.copy()
	draw = ImageDraw.Draw(img)
    for i in range(scroll_no):
	scroll_loc=start_loc
	for x in range(-1*start_loc[0]):
	    print(scroll_loc)

    """

def drawBorder(img, color, justTop=False):
    draw = ImageDraw.Draw(img)
    draw.line((0,0,LED_COLS-1,0),fill=color)
    draw.line((0,LED_ROWS-1,LED_COLS-1,LED_ROWS-1),fill=color)
    if (not justTop):
	draw.line((0,0,0,LED_ROWS-1),fill=color)
	draw.line((LED_COLS-1,0,LED_COLS-1,LED_ROWS-1),fill=color)

if __name__ == '__main__':
    print("Starting!")
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    anim_biFlash(strip,Color(255,0,0,),Color(0,0,255),10,150)
    font = ImageFont.truetype("arial.ttf", 13)
    font2 = ImageFont.truetype("arial.ttf",12)
    print("Displayed")
    pos = 0
    #image = Image.new('RGB',(25,12),color=(100,100,100))
    #drawText(strip, image, "RIP", font, (0,0,0),loc=(3,-1))
    #pushImage(strip,image)
    """
    with open ("pi.txt","r") as pitext:
	pidata=pitext.read().replace('\n','')
    """
    #print(pidata)
    image = Image.new('RGB',(25,12),color=(0,0,20))
    scrollText(strip,image,"TRY OUTDRINKING ME. 508-615-6993 WINNER GETS 50 BUCKS",font,(255,150,0,255),10,2000,loc=(0,-1))
    #image = Image.new('RGB',(25,12),color=(0,0,0))
    #scrollText(strip,image,"A3 DISPLAY",font2,(255,0,0,255),50,200,loc=(0,-1))
    """
  
	#image = Image.new('RGB',(25,12),color=(0,0,20))
	#scrollText(strip, image, "RIP", font, (255,150,0,255), 100, 10)
	
        pos+=0.1
        topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
        topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
        image = Image.new('RGB',(25,12),color=(0,0,20))
        drawText(strip, image, "RIP", font, (255,150,0,255),loc=(3,-1))
        drawBorder(image,topColor)
        pushImage(strip,image)
        time.sleep(1)
        pos+=0.1
        topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
        topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
        image = Image.new('RGB',(25,12),color=(0,0,20))
        drawText(strip, image, "Larry", font2, (155,250,0,255),loc=(1,-1))
        drawBorder(image,topColor)
        pushImage(strip,image)
        time.sleep(1)
	
	draw
    """
    """
    #anim_pulseInterp(strip,Color(255,0,0),Color(0,0,255),1,10000)
           # setPX(strip,x,y,Color(255*x/LED_COLS,255*y/LED_ROWS,90-90*(x/LED_COLS)))
    push(strip)
    time.sleep(15)
    #anim_pulse(strip,Color(255,255,255),10,100)
    wipe(strip,Color(0,0,0))
    """
    print("ending")


