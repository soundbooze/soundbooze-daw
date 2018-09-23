# non-realtime

import os
import threading
import signal
import sys

def CleanUp():
    os.system("rm -f *.wav")
    sys.exit(0)

def SignalExit(signal, frame):
    CleanUp()

#threadLock = threading.Lock()

class capturePlaybackThread (threading.Thread):
   #global threadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      #threadLock.acquire()
      os.system("jack_capture -d 4 -f wav playback.wav > /dev/null 2>&1") 
      #threadLock.release()

class captureGuitarThread (threading.Thread):
   #global threadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      #threadLock.acquire()
      os.system("jack_capture -p system:capture* -d 4 -f wav guitar.wav > /dev/null 2>&1")
      #threadLock.release()

def Initialize():  
    signal.signal(signal.SIGINT, SignalExit)
    signal.signal(signal.SIGTERM, SignalExit)
    signal.signal(signal.SIGQUIT, SignalExit)

    # start threads

    threads = []
    threadPlayback = capturePlaybackThread(1, "Thread-Playback-Extract")
    threadGuitar = captureGuitarThread(2, "Thread-Guitar-Extract")
    threadPlayback.start()
    threadGuitar.start()
    threads.append(threadPlayback)
    threads.append(threadGuitar)

    for t in threads:
        t.join()

if __name__ == "__main__":
    Initialize()
    CleanUp()
