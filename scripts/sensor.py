## TODO:
## real-time audio buffer -> featureX
## audio sound classification
## frame intense / motion -> control

import os
import cv2
import sys
import time
import signal
import threading
import getopt
import numpy as np

threadLock = threading.Lock()

def SignalExit(signal, frame):
  stream.stop_stream()
  stream.close()
  p.terminate()
  cv2.destroyAllWindows()
  sys.Exit(0)

class captureThread (threading.Thread):
   global threadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
       while (1):

          threadLock.acquire()
     
          try:
            #os.system("arecord -D hw:2 -r 48000 -f S16_LE  -t wav -d 1 out.wav > /dev/null 2>&1")
            os.system("./realtime")
          except:
            pass

          threadLock.release()

class videoThread (threading.Thread):

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
       cap = cv2.VideoCapture(1)

       while (1):

          r, frame = cap.read()
          hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

          # define range of blue color in HSV
          lower = np.array([100,50,50])
          upper = np.array([100,255,255])

          # Threshold the HSV image to get only blue colors
          mask = cv2.inRange(hsv, lower, upper)
          if (np.all(mask==0)):
            ts = time.time()
            print ts

          # Bitwise-AND mask and original image
          #res = cv2.bitwise_and(frame,frame, mask= mask)

          cv2.imshow('frame',frame)
          #cv2.imshow('mask',mask)
          #cv2.imshow('res',res)

          k = cv2.waitKey(5) & 0xFF
          if k == 27:
              break

threads = []
thread1 = captureThread(1, "Capture")
thread2 = videoThread(2, "Video")
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

signal.signal(signal.SIGINT, SignalExit)

