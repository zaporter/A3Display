# Supports ability to manipulate PIL images
# Author: Jake Roller


from PIL import Image, ImageFont, ImageDraw
from basicDisp import *
from a3time import *

try:
    from neopixel import *
except ImportError:
    pass


def pushImage(img):
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            col = img.getpixel((x,y))
            setPX(x,y,col)
    push()

def pushImageFile( filename):
    print("Pushing image from file: "+filename)
    img = Image.open(filename)
    pushImage(img)

def drawText( img, text, font, colorRGB, loc=(0,0)):
    print("Drawing text: "+text);
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


def scrollText( img, text, font, colorRGB, wait_ms, scroll_no, loc=(0,0)):
    print("Scrolling text: "+text)
    back_img = img.copy()
    draw = ImageDraw.Draw(img)
    size= draw.textsize(text,font)
    frames=[]
    scroll_loc=(LED_COLS,loc[1])
    
    for pos in range(size[0]+LED_COLS):
        print(str(pos)+"/"+str(size[0]+LED_COLS))
        draw.text(scroll_loc,text,font=font,fill=colorRGB)
        scroll_loc=(scroll_loc[0]-1,scroll_loc[1])
        frames.append(img)
        img = back_img.copy()
        draw = ImageDraw.Draw(img)
    print("render complete")
    for i in range(scroll_no):
        for pos in range(size[0]+LED_COLS):
            pushImage(frames[pos])
            sleep_ms(wait_ms)

def drawBorder(img, color, justTop=False):
    draw = ImageDraw.Draw(img)
    draw.line((0,0,LED_COLS-1,0),fill=color)
    draw.line((0,LED_ROWS-1,LED_COLS-1,LED_ROWS-1),fill=color)
    if (not justTop):
        draw.line((0,0,0,LED_ROWS-1),fill=color)
        draw.line((LED_COLS-1,0,LED_COLS-1,LED_ROWS-1),fill=color)

def displayText(text, text_color, bg_color, speed):
    print("Displaying text: "+text)
    """Renders scrolling text in helvetic font with a given bg and text color (R, G, B) and a given update speed"""
    font = ImageFont.truetype("fonts/helvetica.ttf", 14)
    image = Image.new('RGB',(LED_COLS,LED_ROWS),color=bg_color)
    scrollText( image, text.upper(), font, text_color, speed, 2000000, loc=(0,1))




