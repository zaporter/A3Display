anim_biFlash(strip,Color(200,0,0,),Color(0,0,200),10,150)
font = ImageFont.truetype("fonts/helvetica.ttf", 15)
image = Image.new('RGB',(25,12),color=(0,0,20))
scrollText(strip,image,"Text-Here",font,(255,150,0,255),10,2000,loc=(0,-1))
