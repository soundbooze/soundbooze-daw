import sounddevice as sd
import soundfile as sf
import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import time

time.sleep(1)

print 'Ready ...'

sd.default.samplerate = 44100
sd.default.channels = 1
sd.default.device = 5

fs = sd.default.samplerate
duration = 5

data = sd.rec(duration * fs, blocking=True)

filename = 'u.wav'

sf.write(filename, data, sd.default.samplerate)

data, sr = librosa.load(filename)

loudness = vamp.collect(data, sr, "vamp-libxtract:loudness")
vector = loudness['vector']

P = vector[1]
print P.size

plt.plot(P)
plt.show()
