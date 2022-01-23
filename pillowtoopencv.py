import cv2
import numpy as np
from PIL import Image
img=Image.open("media\\img01.jpg")
img.show()
cv2.namedWindow("OpenCV")
img=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
cv2.imshow("OpenCV",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
