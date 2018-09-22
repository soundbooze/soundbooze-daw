import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
y, sr = librosa.load('wav/input.wav')
C = librosa.cqt(y, sr=sr)

librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), sr=sr, x_axis='time', y_axis='cqt_note')
plt.colorbar(format='%+2.0f dB')
plt.title('Constant-Q power spectrum')
plt.tight_layout()
plt.show()

# Limit the frequency range

C = librosa.cqt(y, sr=sr, fmin=librosa.note_to_hz('C2'), n_bins=60)

# Using a higher frequency resolution

C = librosa.cqt(y, sr=sr, fmin=librosa.note_to_hz('C2'), n_bins=60 * 2, bins_per_octave=12 * 2)
