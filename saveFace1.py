import cv2
casc_path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(casc_path)
image=cv2.imread("media\\person3.jpg")
faces=faceCascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)#detect result
imgheight=image.shape[0]
imgwidth=image.shape[1]
count=1
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(128.255,0),2)#select face
    filename="output\\face"+str(count)+".jpg"#save file
    image1=image[y:y+h,x:x+w]
    image2=cv2.resize(image1,(400,400))
    cv2.imwrite(filename,image2)
    count+=1