import cv2
cv2.namedWindow("Image",cv2.WINDOW_FULLSCREEN)
cv2.namedWindow("Image2",cv2.WINDOW_FULLSCREEN)
img=cv2.imread("media\\img01.jpg",0)#1 Color read 0 gray read -1 origin read
img2=cv2.imread("media\\img01.jpg",1)
cv2.imshow("Image",img)
cv2.imshow("Image2",img2)
cv2.waitKey(2000)
cv2.destroyWindow("Image")
cv2.destroyWindow("Image2")