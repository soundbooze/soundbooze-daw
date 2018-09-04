import numpy as np
import cv2
from skimage import util, filters

def __threshold_moving(input, last_image):
        if (last_image.shape == input.shape):
            output =  cv2.absdiff(input, last_image)
        else:
            output = numpy.ndarray(shape=input.shape, dtype=input.dtype)
        return input, output

cap = cv2.VideoCapture(1)
ret,old_frame = cap.read()

old_frame_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
old_sobel = util.invert(old_frame_gray)

while(1):

    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobel = util.invert(frame_gray)

    m = __threshold_moving(old_sobel, sobel)
    print np.round(m, 5)

    cv2.imshow('frame', sobel)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    old_gray = frame_gray.copy()

cv2.destroyAllWindows()
cap.release()
