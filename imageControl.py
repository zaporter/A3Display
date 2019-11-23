# Supports ability to manipulate PIL images
# Author: Jake Roller


from PIL import Image, ImageFont, ImageDraw
from neopixel import *
from basicDisp import *
from a3time import *



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
    for i in range(scroll_no):
	scroll_loc=(LED_COLS,loc[1])
	for x in range(size[0]+LED_COLS):
	    draw.text(scroll_loc,text,font=font,fill=colorRGB)
	    scroll_loc=(scroll_loc[0]-1,scroll_loc[1])
	    pushImage(strip,img)
	    img = back_img.copy()
	    draw = ImageDraw.Draw(img)
	    sleep_ms(wait_ms)

def drawBorder(img, color, justTop=False):
    draw = ImageDraw.Draw(img)
    draw.line((0,0,LED_COLS-1,0),fill=color)
    draw.line((0,LED_ROWS-1,LED_COLS-1,LED_ROWS-1),fill=color)
    if (not justTop):
	draw.line((0,0,0,LED_ROWS-1),fill=color)
	draw.line((LED_COLS-1,0,LED_COLS-1,LED_ROWS-1),fill=color)
