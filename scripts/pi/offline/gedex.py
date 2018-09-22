import vamp
import librosa
import numpy as np
import matplotlib.pyplot as plt
import time

data, sr = librosa.load('u.wav')

loudness = vamp.collect(data, sr, "vamp-libxtract:loudness")
ssharpness = vamp.collect(data, sr, "vamp-libxtract:sharpness")

vectorL = loudness['vector']
vectorS = loudness['vector']

L = vectorL[1]
SS = vectorL[1]

plt.plot(SS)
plt.show()

print ssharpness

# todo:
# envelope
