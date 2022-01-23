from PIL import Image
img=Image.open("media\\img01.jpg")
imggray=img.convert("L")#Convert to gray scale
imggray.save("output\\gray01.jpg")