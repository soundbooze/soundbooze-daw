import cv2
import numpy as np
from skimage import data, io, util, color, filters, segmentation, exposure, feature

def coordinate_print(frame):
   '''
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray,(5,5),0)
   ret, thresh_img = cv2.threshold(blur, 107, 125, cv2.THRESH_BINARY)
   contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]

   for c in contours:
       cv2.drawContours(frame, [c], -1, (5,5,5), 3)

   if (len(contours) > 0):
     cnt = contours[0]
     coord = cnt[0][0]
     print coord[0], coord[1]
   '''

def have_motion(frame1, frame2):
    if frame1 is None or frame2 is None:
            return False

    delta = cv2.absdiff(frame1, frame2)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]

    t = int(np.asscalar(np.sum(thresh)))

    if (t > 4300000):
        print t

    #return np.sum(thresh) > 0 

cap = cv2.VideoCapture(1)

while(1):

    _, frame1 = cap.read()
    _, frame2 = cap.read()

    have_motion(frame1, frame2)
    
    gray = color.rgb2gray(frame1)

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    invert = util.invert(gray)
    edges = filters.sobel(gray)
    scharr = filters.scharr(invert)

    '''
    for i in range(len(scharr)):
        for j in range(len(scharr[i])):
            print(scharr[i][j])
            #scharr[i][j] = scharr[i][j] + 45
    '''

    cv2.imshow('main', frame1)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release
cv2.destroyAllWindows()
