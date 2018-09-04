import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
   ret, frame = cap.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray,(5,5),0)
   ret, thresh_img = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

   contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
   for c in contours:
       cv2.drawContours(frame, [c], -1, (5,5,5), 3)

   if (len(contours) > 0):
     cnt = contours[0]
     coord = cnt[0][0]
     print coord[0], coord[1]

   cv2.imshow('frame', gray)

   if cv2.waitKey(1) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
