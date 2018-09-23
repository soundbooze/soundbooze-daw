import threading

handlerThreadLock = threading.Lock()

class CaptureThread (threading.Thread):
   global handlerThreadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      handlerThreadLock.acquire()
      print 'Capture ...'
      handlerThreadLock.release()

class ProcessThread (threading.Thread):
   global handlerThreadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      handlerThreadLock.acquire()
      print 'Process ...'
      handlerThreadLock.release()

while (True):

    threads = []

    thread1 = CaptureThread(1, "Thread-Playback-Extract")
    thread2 = ProcessThread(2, "Thread-Guitar-Extract")

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()
