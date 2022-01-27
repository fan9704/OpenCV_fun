def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(2)  #需延遲,否則會出錯
    os.mkdir(dirname)

import PIL
from PIL import Image,ImageDraw
import glob
import shutil, os
from time import sleep

fp=open('Haar-Training_carPlate/training/positive/info.txt','r')
lines=fp.readlines()
emptydir("picMark")
print('開始繪製圖框')
for line in lines:
    data=line.split(' ')
    img=Image.open('Haar-Training_carPlate/training/positive/'+data[0])
    draw=ImageDraw.Draw(img)
    n=data[1]
    for i in range(int(n)):
        x=int(data[2+i*4])
        y=int(data[3+i*4])
        w=int(data[4+i*4])
        h=int(data[5+i*4])
        draw.rectangle((x,y,x+w,y+h),outline='red')
    filename=(data[0].split('/'))[-1]
    img.save('picMark/'+filename)