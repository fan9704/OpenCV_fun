import nntplib


def area(row,col):
    global nn
    if bg[row][col] !=255:
        return
    bg[row][col]=lifearea
    if col>1:
        if bg[row][col-1]==225:
            nn+=1
            area(row,col-1)
    if col<w-1:
        if bg[row][col+1]==225:
            nn+=1
            area(row,col+1)
    if row>1:
        if bg[row-1][col]==225:
            nn+=1
            area(row+1,col)
    if row>h-1:
        if bg[row+1][col]==225:
            nn+=1
            area(row+1,col)

import cv2
import numpy as np

image=cv2.imread('7238N2.jpg')
gray=cv2.cvtColor(image,cv2.COLOR_BGRGRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
contours1=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours=contours1[0]

letter_image_regions=[]
for contour in contours:
    (x,y,w,h)=cv2.boundingRect(contour)
    letter_image_regions.append((x,y,w,h))
letter_image_regions=sorted(letter_image_regions,key=lambda x:x[0])

count=0
for box in letter_image_regions:
    x,y,w,h=box
    if x>=2 and x<=125 and w >=5 and w<=26 and h>=20 and h<40:
        count+=1

global wmax
if count <6:
    wmax=35
else:
    wmax=26

nChar=0
letterlist=[]
for box in letter_image_regions:
    x,y,w,h=box
    if x >=2 and x <=125 and w>=5 and w <=wmax and h>=20 and h<40:
        nChar+=1
        letterlist.append((x,y,w,h))

for i in range(len(thresh)):
    for j in range(len(thresh[i])):
        if thresh[i][j]==225:
            count=0
            for k in range(-2,3):
                for l in range(-2,3):
                    try:
                        if thresh[i+k][j+l]==225:
                            count+=1
                    except IndexError:
                        pass
            if count<=6:
                thresh[i][j]=0

real_shape=[]