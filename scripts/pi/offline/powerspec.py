# http://python-sounddevice.readthedocs.io/en/0.3.7/examples.html
# list device number
# python -m sounddevice

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

# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs, device=7)
# status = sd.wait()

data, sr = librosa.load(filename)

power_spectrum = vamp.collect(data, sr, "vamp-example-plugins:powerspectrum")
matrix = power_spectrum['matrix']
P = matrix[1]

# np.ndarray (431, 513)
# print type(power_array)


#print P.cumsum()[-1]
#print P.sum()

plt.imshow(P)
plt.show()
