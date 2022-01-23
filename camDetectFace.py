import cv2
cv2.namedWindow("frame")
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    ret,img=cap.read()
    casc_path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
    faceCascade=cv2.CascadeClassifier(casc_path)
    if ret ==True:
        faces=faceCascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)#detect result
        imgheight=img.shape[0]
        imgwidth=img.shape[1]
        cv2.rectangle(img,(10,imgheight-20),(110,imgheight),(0,0,0),-1)
        cv2.putText(img,"Find"+str(len(faces))+" face!",(10,imgheight-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        for (x,y,w,h) in faces:#faces is ARRAY
            cv2.rectangle(img,(x,y),(x+w,y+h),(128,255,0),2)
        cv2.imshow("frame",img)
        k=cv2.waitKey(100)
        if k==ord("z") or k==ord("Z"):
            cv2.imwrite("output\\catch.jpg",img)
            break
cap.release()
cv2.destroyWindow("frame")