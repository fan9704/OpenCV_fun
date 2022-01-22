from email.mime import image
import cv2
from cv2 import imread
img=imread("media\\person1.jpg")
print("img.shape=",img.shape)
cv2.imshow("win1",img)
x,y,w,h=341,76,125,125
face=img[y:y+h,x:x+w]

for row in range(y,y+h):
    for col in range(x,x+w):
        print(img[row,col],end=" ")
print()
for row in range(y,y+h):
    for col in range(x,x+w):
        img[row,col][0]=0
        img[row,col][1]=50
cv2.imshow("win2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()