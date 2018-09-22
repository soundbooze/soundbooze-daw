import vamp
import librosa
import essentia.standard as es
import matplotlib.pyplot as plt 

audio_file = 'uduk.wav'

loader = es.MonoLoader(filename=audio_file, downmix = 'mix', sampleRate = 22050)
audio = loader()

audio, sr = librosa.load(audio_file, sr=44100, mono=True)

data = vamp.collect(audio, sr, "mtg-melodia:melodia")

hop, melody = data['vector']
print(hop)
print(melody)

import numpy as np
timestamps = 8 * 128/44100.0 + np.arange(len(melody)) * (128/44100.0)

params = {"minfqr": 100.0, "maxfqr": 800.0, "voicing": 0.2, "minpeaksalience": 0.0}

data = vamp.collect(audio, sr, "mtg-melodia:melodia", parameters=params)
hop, melody = data['vector']


plt.figure(figsize=(18,6))
plt.plot(timestamps, melody)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

melody_pos = melody[:]
melody_pos[melody<=0] = None
plt.figure(figsize=(18,6))
plt.plot(timestamps, melody_pos)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.show()

melody_cents = 1200*np.log2(melody/55.0)
melody_cents[melody<=0] = None
plt.figure(figsize=(18,6))
plt.plot(timestamps, melody_cents)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (cents relative to 55 Hz)')
plt.show()
