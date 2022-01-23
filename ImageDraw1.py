from PIL import Image,ImageDraw,ImageFont

img=Image.new("RGB",(300,400),"lightgray")
drawimg=ImageDraw.Draw(img)

drawimg.ellipse((50,50,250,250),width=3,outline="gold")
drawimg.polygon([(100,90),(120,130),(80,130)],fill="brown",outline="red")
drawimg.polygon([(200,90),(220,130),(180,130)],fill="brown",outline="red")
drawimg.rectangle((140,140,160,180),fill="blue",outline="black")
drawimg.ellipse((100,200,200,220),fill="red")
drawimg.text((130,280),"e-happy",fill="orange")
myfont=ImageFont.truetype("C:\Windows\Fonts\msjh.ttc",16)
drawimg.text((110,320),"文淵閣工作室",fill="red",font=myfont)
img.show()
img.save("output\\happyface.jpg")