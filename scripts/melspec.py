import librosa
import librosa.display
import numpy as np

y, sr = librosa.load("playback.wav")
librosa.feature.melspectrogram(y=y, sr=sr)
# array([[  2.891e-07,   2.548e-03, ...,   8.116e-09,   5.633e-09],
# [  1.986e-07,   1.162e-02, ...,   9.332e-08,   6.716e-09],
# ...,
# [  3.668e-09,   2.029e-08, ...,   3.208e-09,   2.864e-09],
# [  2.561e-10,   2.096e-09, ...,   7.543e-10,   6.101e-10]])

# Using a pre-computed power spectrogram

D = np.abs(librosa.stft(y))**2
S = librosa.feature.melspectrogram(S=D)

# Passing through arguments to the Mel filters
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                    fmax=8000)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
librosa.display.specshow(librosa.power_to_db(S,
                                             ref=np.max),
                         y_axis='mel', fmax=8000,
                         x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()
plt.show()
