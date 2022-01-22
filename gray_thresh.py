import cv2
from cv2 import threshold
from cv2 import THRESH_BINARY
from numpy import imag
def show(image):
    for y in range(8,14):
        for x in range(6,10):
            print(image[y,x],end=" ")
        print()
    print()

img=cv2.imread("media\\face.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("gray.shape=",gray.shape)
show(gray)

_,thresh=cv2.threshold(gray,187,255,cv2.THRESH_BINARY)#Black White Convert
print("thresh.shape=",thresh.shape)
show(thresh)

gray2=cv2.imread("media\\face.jpg",0)
print("gray2.shape=",gray2.shape)
show(gray2)

_,thresh2=cv2.threshold(gray2,187,200,cv2.THRESH_BINARY_INV)
print("thresh.shape=",thresh.shape)
show(thresh2)
