from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt 

y, sr = librosa.load('../wav/uduk.wav')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=12, n_fft=4096)
chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)

plt.figure()
plt.subplot(2,1,1)
librosa.display.specshow(chroma_stft, y_axis='chroma')

plt.title('chroma_stft')
plt.colorbar()
plt.subplot(2,1,2)
librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')

plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()

plt.show()
