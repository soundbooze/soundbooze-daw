import numpy as np
import cv2
from skimage import util, filters

import time
import rtmidi

midiout = rtmidi.MidiOut()
midiout.open_port(0)

cap = cv2.VideoCapture(1)
ret,old_frame = cap.read()

old_frame_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
old_sobel = util.invert(old_frame_gray)

def RecordToggle():
    global cap

    cv2.destroyAllWindows()
    cap.release()

    note_on = [0x90, 60, 115]
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)
    time.sleep(0.2)
    midiout.send_message(note_off)

    time.sleep(1)

    cap = cv2.VideoCapture(1)
    ret,old_frame = cap.read()

def __threshold_moving(input, last_image):
    if (last_image.shape == input.shape):
        output =  cv2.absdiff(input, last_image)
    else:
        output = numpy.ndarray(shape=input.shape, dtype=input.dtype)
    return input, output

def Loop():
    global cap

    while(1):

        ret,frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobel = util.invert(frame_gray)

        m = __threshold_moving(old_sobel, sobel)

        # naive - TODO: - movement <-- valChange
        #               - rnd var / ...process ? hmm, .. /stat inf
        #               - tap to enable/disable

        i, o = m
        sum_nd = int(np.sum(o)/750000)
        #print sum_nd

        #print np.cumsum(oo)
        #oo = np.resize(o, (10, 10))
        #print oo.shape, oo.size
        #print  np.std(oo, axis=0)
        #print  np.sum(np.var(oo, axis=0))
        #print np.cumprod(oo)
        # naive

        #cv2.imshow('frame', sobel)
        print sum_nd

        if (sum_nd < 2):
            RecordToggle()

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        old_gray = frame_gray.copy()

Loop()

cv2.destroyAllWindows()
cap.release()

del midiout
