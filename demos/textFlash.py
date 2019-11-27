

font = ImageFont.truetype("fonts/arial.ttf", 13)
font2 = ImageFont.truetype("fonts/arial.ttf", 10)
pos =0.0
while True:
    pos+=0.1
    topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
    topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
    image = Image.new('RGB',(25,12),color=(0,0,20))
    drawText(strip, image, "A3", font, (255,150,0,255),loc=(5,-1))
    drawBorder(image,topColor, justTop=True)
    pushImage(strip,image)
    sleep_ms(strip,1000)
    pos+=0.1
    topColor = ((256*math.cos(pos), 256*math.cos(pos + 2), 256*math.cos(pos - 2)))
    topColor = (int(topColor[0]), int(topColor[1]),int(topColor[2]))
    image = Image.new('RGB',(25,12),color=(0,0,20))
    drawText(strip, image, "Larry", font2, (155,250,0,255),loc=(1,-1))
    drawBorder(image,topColor, justTop=True)
    pushImage(strip,image)
    sleep_ms(strip,1000)

