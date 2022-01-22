from random import randrange
import cv2
import numpy as np

canvas=np.ones((200,250,3),dtype="uint8")#h w mode 3=BGR
print(canvas.shape)
canvas[:]=(125,40,255)#magenta color give
cv2.imshow('canvas',canvas)

bg=np.zeros((200,250,1),np.uint8)#h w mode 1=grayscale
print(bg.shape)
bg.fill(255)#white color give

for j in range(200):
    for i in range(250):
        bg[j][i].fill(255-i)

cv2.imshow("bg",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()