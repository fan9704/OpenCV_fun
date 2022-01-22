import cv2
cv2.namedWindow("ShowImage")
image=cv2.imread("media\\img01.jpg",0)
cv2.imshow("ShowImage",image)
cv2.imwrite("output\\img01copy1.jpg",image)#Q95
cv2.imwrite("output\\img01copy2.jpg",image,[int(cv2.IMWRITE_JPEG_QUALITY),50])#50