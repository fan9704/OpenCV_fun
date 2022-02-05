import glob
import os
import shutil
from time import sleep
from PIL import Image
import PIL
import numpy as np
import cv2
def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)
    os.mkdir(dirname)

print("開始擷取車牌!")
print("無法擷取車牌圖片:")
dstdir='cropPlate'
emptydir(dstdir)
myfiles=glob.glob("predictPlate\*.JPG")
for imgname in myfiles:
    filename=(imgname.split("\\"))[-1]
    img=cv2.imread(imgname)
    detector=cv2.CascadeClassifier('haar_carplate.xml')
    signs=detector.detectMultiScale(img,scaleFactor=1.1,minNeighbors=4,minSize=(20,20))
    if len(signs)>0:
        for (x,y,w,h)  in signs:
            image1=Image.open(imgname)
            image2=image1.crop((x,y,x+w,y+h))
            image3=image2.resize((140,40),Image.ANTIALIAS)
            img_gray=np.array(image3.convert('L'))
            _,img_thre=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
            cv2.imwrite(dstdir+'/'+filename,img_thre)
    else:
        print(filename)
print("擷取車牌結束")