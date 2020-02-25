# Supports ability to manipulate PIL images
# Author: Jake Roller


from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageSequence
from basicDisp import *
from a3time import *

try:
    from neopixel import *
except ImportError:
    pass

def resizeImage(img):
    img.thumbnail((LED_COLS+1,LED_ROWS+1))

def pushImage(img):
#    resizeImage(img)
    img.thumbnail((LED_COLS,LED_ROWS),Image.ANTIALIAS)
    for x in range(LED_COLS):
        for y in range(LED_ROWS):
            if (x<img.size[0] and y<img.size[1]):
                col = img.getpixel((x,y))
            else:
                col = (0,0,0)
            setPX(x,y,col)
    push()

def pushImageFile( filename):
    print("Pushing image from file: "+filename)
    img = Image.open(filename)
    pushImage(img)

def pushGIFFile(filename,loops=1,wait=50):
    try:
        im = Image.open(filename)
    except IOError:
        print("Cannot load: "+filename)
        return
    palette = im.getpalette()
    for k in range(loops):
        im.seek(0)
        try:
            while 1:
                im.putpalette(palette)
                new_im = Image.new("RGBA",im.size)
                new_im.paste(im)
                pushImage(new_im)
                im.seek(im.tell()+1)
                sleep_ms(wait)

        except EOFError:
            pass

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

def dropText(img, text, font, colorRGB, wait_ms, scroll_no, bottomMax=(255,255,255)):
    print("Dropping text: "+text)
    back_img=img.copy();
    draw = ImageDraw.Draw(img)
    size = draw.textsize(text,font)
    for k in range(scroll_no):
        scroll_loc = (int(LED_COLS/2.0-size[0]/2.0),-size[1])
        for pos in range(LED_ROWS-1):
            draw.text(scroll_loc,text,font=font, fill=colorRGB)
            scroll_loc=(scroll_loc[0],scroll_loc[1]+1)
            pushImage(img)
            sleep_ms(wait_ms)
            img=back_img.copy()
            draw = ImageDraw.Draw(img)

def flashText(text, textColor1, textColor2, bgColor1, bgColor2, speed=10, loop=1000, loc=(0,1), size=14):
    # Flash the background and the text
    font = ImageFont.truetype("fonts/helvetica.ttf", size)
    bgImage1 = Image.new('RGB',(LED_COLS,LED_ROWS), color=bgColor1)
    bgImage2 = Image.new('RGB',(LED_COLS,LED_ROWS), color=bgColor2)
    frames = []

    draw = ImageDraw.Draw(bgImage1)
    size = draw.textsize(text, font)
    draw.text((loc[0],loc[1]), text, font=font, fill=textColor1)
    frames.append(bgImage1)

    draw = ImageDraw.Draw(bgImage2)
    draw.text((loc[0],loc[1]), text, font=font, fill=textColor2)
    frames.append(bgImage2)

    for i in range(2*loop):
        pushImage(frames[i%2])
        sleep_ms(speed)


def defaultText(text, textColor=(0, 0, 0), bgColor=(200, 200, 200), speed=1, loop=1000, size=14):
    # Wrapper for scrollText with less mandatory inputs
    font = ImageFont.truetype("fonts/helvetica.ttf", size)
    image = Image.new('RGB',(LED_COLS,LED_ROWS),color=bgColor)
    scrollText(image, text, font, textColor, speed, loop, loc=(0,1))

def drawBorder(img, color, justTop=False):
    draw = ImageDraw.Draw(img)
    draw.line((0,0,LED_COLS-1,0),fill=color)
    draw.line((0,LED_ROWS-1,LED_COLS-1,LED_ROWS-1),fill=color)
    if (not justTop):
        draw.line((0,0,0,LED_ROWS-1),fill=color)
        draw.line((LED_COLS-1,0,LED_COLS-1,LED_ROWS-1),fill=color)




