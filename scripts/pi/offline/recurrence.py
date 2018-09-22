from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt 

y, sr = librosa.load('../wav/solo.wav')

mfcc = librosa.feature.mfcc(y=y, sr=sr)

R = librosa.segment.recurrence_matrix(mfcc)
R_aff = librosa.segment.recurrence_matrix(mfcc, mode='affinity')

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
librosa.display.specshow(R, x_axis='time', y_axis='time')

plt.title('Binary recurrence (symmetric)')
plt.subplot(1, 2, 2)
librosa.display.specshow(R_aff, x_axis='time', y_axis='time', cmap='magma_r')

plt.title('Affinity recurrence')
plt.tight_layout()

plt.show()
