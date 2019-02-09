import os
import threading

class PlaybackThread (threading.Thread):

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      playback = "jack_capture -p 'PulseAudio JACK Sink:front*' -f wav playback.wav" 
      os.system(playback)

class GuitarThread (threading.Thread):

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      guitar = "jack_capture -p jack_thru:output* -f wav guitar.wav"
      os.system(guitar)

os.system("rm -f *.wav")

threads = []

thread1 = PlaybackThread(1, "Thread-Playback")
thread2 = GuitarThread(2, "Thread-Guitar")

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print ''
