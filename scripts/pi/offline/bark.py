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

bark_coefficients = vamp.collect(data, sr, "vamp-libxtract:bark_coefficients")

matrix = bark_coefficients['matrix']
P = matrix[1]

'''
sementara - lihat sonic visualiser
plt.yscale('log')
plt.plot(abs(P));
plt.show()
'''
