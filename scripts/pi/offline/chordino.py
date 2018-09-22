import vamp
import librosa
import essentia.standard as es
import matplotlib.pyplot as plt 

audio_file = 'solo.wav'

loader = es.MonoLoader(filename=audio_file, downmix = 'mix', sampleRate = 44100)
audio = loader()

audio, sr = librosa.load(audio_file, sr=44100, mono=True)

data = vamp.collect(audio, sr, "nnls-chroma:chordino")

idx = 0
for i in data['list']:
    print(data['list'][idx]['label'])
    idx = idx + 1

#print(data['list'][0]['timestamp'])

'''
timestamp, label = data['list']

print(timestamp)
print(label)
'''
