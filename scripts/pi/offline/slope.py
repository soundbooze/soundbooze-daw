# bersamaan dengan pitch/note [yin/melodia] tracker

import sounddevice as sd
import soundfile as sf
import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import time

sd.default.samplerate = 44100
sd.default.channels = 1
sd.default.device = 5

sr = sd.default.samplerate

filename = 'u.wav'

data, sr = librosa.load(filename)

sslope_vector = vamp.collect(data, sr, "vamp-libxtract:spectral_slope")
v = sslope_vector['vector']
P = v[1]

plt.plot(P)
plt.show()
