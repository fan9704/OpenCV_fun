import cv2,glob
from cv2 import threshold
import numpy as np

files=glob.glob('cropMono\*.jpg')#all file
n=len(files)
spaceX=10#left padding
spaceY=8#top padding
offset=1#margin of every char
img=cv2.imread(files[0])
h,w=img.shape[0],img.shape[1]

bg=np.zeros((h+2*spaceY,(w+offset)*n+2*spaceX,1),np.uint8)
bg.fill(255)

for m,file in enumerate(files):
    gray=cv2.imread(file,0)
    _,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#Convert to black white
    for row in range(h):
        for col in range(w):
            bg[spaceY+row][spaceX+col+(w+offset)*m]=thresh[row][col]#shortcut picture
    cv2.imwrite('merge.jpg',bg)#save

merge=cv2.imread("merge.jpg")
cv2.imshow("merge",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()