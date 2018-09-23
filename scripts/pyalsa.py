'''
pcm.!default {
    type hw
    card 2
}

ctl.!default {
    type hw
    card 2
}
'''
import alsaaudio
import numpy as np
import aubio

# constants
samplerate = 48000
framesize = 1024

recorder = alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE, device="hw:2")
recorder.setperiodsize(framesize)
recorder.setrate(samplerate)
recorder.setformat(alsaaudio.PCM_FORMAT_S16_LE)
recorder.setchannels(1)

while True:
    try:
        _, data = recorder.read()
        samples = np.fromstring(data, dtype=aubio.float_type)
        for s in samples:
            print s

    except KeyboardInterrupt:
        break

