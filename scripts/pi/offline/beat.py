from __future__ import print_function
import librosa
import matplotlib.pyplot as plt 
import numpy as np

y1, sr1 = librosa.load('s.wav')
y2, sr2 = librosa.load('t.wav')

tempo1, beat_frames1 = librosa.beat.beat_track(y=y1, sr=sr1)
tempo2, beat_frames2 = librosa.beat.beat_track(y=y2, sr=sr2)

x1 = np.arange(len(beat_frames1))
x2 = np.arange(len(beat_frames2))

len1 = len(beat_frames1)
len2 = len(beat_frames2)

print(len1, len2)

plt.figure(1)

plt.subplot(211)
plt.xlabel('x1')
plt.ylabel('y1')
plt.title('Tempo ' + format(tempo1))
plt.bar(x1, beat_frames1, align='center', alpha=0.5)

plt.subplot(212)
plt.xlabel('x2')
plt.ylabel('y2')
plt.title('Tempo ' + format(tempo2))
plt.bar(x2, beat_frames2, align='center', alpha=0.5)

corr = np.correlate(beat_frames1, beat_frames2)
plt.scatter(beat_frames1, beat_frames2, color='r')

plt.show()

'''if
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
'''
