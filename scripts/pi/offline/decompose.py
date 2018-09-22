import sounddevice as sd
import soundfile as sf
import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import time

filename = 'u.wav'

data, sr = librosa.load(filename)

loudness = vamp.collect(data, sr, "vamp-libxtract:loudness")
vector = loudness['vector']

P = vector[1]

plt.plot(P)

# auto freq - adjustment until pattern spotted???
result = sm.tsa.seasonal_decompose(P, freq=20)
result.plot()

plt.show()

