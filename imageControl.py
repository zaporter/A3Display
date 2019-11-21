

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
