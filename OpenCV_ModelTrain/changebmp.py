from PIL import Image
import glob
import os

myfiles=glob.glob("carPlate/*.JPG")
print("開始轉換圖形格式")
for f in myfiles:
    namesplit=f.split("\\")
    img=Image.open(f)
    outname=namesplit[1].replace("resizejpg","bmpraw")
    outname=outname.replace(".jpg",".bmp")
    img.save("carPlate/"+outname,"bmp")
    os.remove(f)
print("轉換圖形格式結束")