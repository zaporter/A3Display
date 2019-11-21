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
