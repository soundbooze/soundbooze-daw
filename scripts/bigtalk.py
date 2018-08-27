
'''

# Big talk this

semi-continuous (todo) 

-- min (externalShell) - min(directApi) -- pre-selected dominantFeatures
-- randomForest ?? genre accuracy
-- re -dataset builder (as small as possible) - [youtube crawler - clever thumbnailer] (min(duration))
-- non-mainstream mfcc &/ classifier
-- [buffer autogrow][buffer lseek][rr] total real-time (pre native)
                                   |--- measure   
-- no non-sense eeeeee /zatlab blablabla citing

high talk bonus:

- normalised image (various amps) learning -> auto knob adjustment

                   deprogrammer breaks free (tmpfs-mmap zeroCopy) <- port all if possible
[------------] | | [------------]      [------------] 
[  capture   ] | | [  capture   ] \    [  capture   ] 
[------------] |l| [------------]  \   [------------] 
      \        |o|                  \                 ...  
       \       |o| [------------]    \ [------------] 
        \-----=|p| [  process   ]      [  process   ] 
               | | [------------]      [------------] 
'''

import os
import sys
import signal
import threading

import librosa
import librosa.beat
import librosa.onset

import numpy as np

import yaml

CBLUE   = '\033[34m'
CRED = '\033[31m'
CYELLOW = '\033[33m'
CEND    = '\033[0m'

SILENT_THRESHOLD = -51

JACK_CAPTURE = "/usr/bin/jack_capture"
CAPTURE_DURATION = 4
PLAYBACK_WAV = "playback.wav"
PLAYBACK_22050 = "playback-22050.wav"
GUITAR_WAV = "guitar.wav"

FFMPEG = "/usr/bin/ffmpeg"
ESSENTIA_EXTRACTOR = "/usr/local/bin/essentia_streaming_extractor_music"

tidakPuas = True

y1 = []
y2 = []
sr1 = 0
sr2 = 0

threadLock = threading.Lock()

def Initialize():  
    signal.signal(signal.SIGINT, SignalExit)

def CaptureLoad():
    global y1
    global y2
    global sr1
    global sr2

    print '[Capture]'

    os.system("(" + str(JACK_CAPTURE) + " -d " + str(CAPTURE_DURATION) + " -f wav " + str(PLAYBACK_WAV) + " > /dev/null 2>&1) | (" + 
                    str(JACK_CAPTURE) + " -p system:capture* -d " + str(CAPTURE_DURATION) + " -f wav " + str(GUITAR_WAV) + " > /dev/null 2>&1)")

    # guitar silence removal
    # os.system("sox guitar.wav guitar-trim.wav silence 1 0.1 1% -1 0.1 1%")

    y1, sr1 = librosa.load(PLAYBACK_WAV)
    y2, sr2 = librosa.load(GUITAR_WAV)

def EstimatedB():
    global y1
    global y2

    S1 = np.abs(librosa.stft(y1))
    S2 = np.abs(librosa.stft(y2))

    ypow1 = librosa.power_to_db(S1**2)
    ypow2 = librosa.power_to_db(S2**2)

    system = np.average(ypow1)
    guitar = np.average(ypow2)

    if (system <= SILENT_THRESHOLD and guitar <= SILENT_THRESHOLD):
      return -1

    else :
      fs = '[Playback]: ' + repr(system) + ' db'
      print fs

      fg = '[Guitar]: ' + repr(guitar)  + ' db'
      print fg

      dist = CYELLOW + '[Distance]: ' + repr(system - guitar) + ' db' + CEND
      print dist

      ## todo: distance tolerance [riff/rhy mel] --via dynProg

      return 0

def EstimateTempo():
    global y1
    global y2
    global sr1
    global sr2

    tempo1, beat_frames1 = librosa.beat.beat_track(y=y1, sr=sr1)
    tempo2, beat_frames2 = librosa.beat.beat_track(y=y2, sr=sr2)

    tempo = CBLUE + '[Tempo]: ' + repr(tempo1) + ' bpm' + CEND
    print tempo

def DetectGenre():
    print '' 
    print CRED + '[Genre:]' + CEND
    os.system(str(FFMPEG) + " -y -i " + str(PLAYBACK_WAV) + " -ar 22050 -ac 1 " + str(PLAYBACK_22050))
    # tmp
    os.system("cd /home/oche/arduino/dataset/genreXpose/genreXpose/ && python tester.py")

def DetectPlaybackChange():
    # feature score: tempo avg, genre, silent event++ ... -- via non-deep/fast classify
    print ''

class extractPlaybackThread (threading.Thread):
   global threadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      threadLock.acquire()
      os.system(str(ESSENTIA_EXTRACTOR) + " " + str(PLAYBACK_WAV) + " playback.yaml > /dev/null 2>&1")
      threadLock.release()

class extractGuitarThread (threading.Thread):
   global threadLock

   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      threadLock.acquire()
      os.system(str(ESSENTIA_EXTRACTOR) + " " + str(GUITAR_WAV) + " guitar.yaml > /dev/null 2>&1")
      threadLock.release()

def EssentiaMusicExtractor():
    print ''
    print '[Essentia]'

    # via API - faster ?

    threads = []

    thread1 = extractPlaybackThread(1, "Thread-Playback-Extract")
    thread2 = extractGuitarThread(2, "Thread-Guitar-Extract")

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()

    print ''
 
def ParseYAML(filename):
    with open(filename, 'r') as stream:
        try:
            data = yaml.load(stream)
            avg_loudness = data['lowlevel']['average_loudness']
            spec_energy_high = data['lowlevel']['spectral_energyband_high']['mean']
            spec_energy_low = data['lowlevel']['spectral_energyband_low']['mean']
            spec_energy_mid_high = data['lowlevel']['spectral_energyband_middle_high']['mean']
            spec_energy_mid_low = data['lowlevel']['spectral_energyband_middle_low']['mean']

            rhythm_bpm = data['rhythm']['bpm']
            rhythm_onsetrate = data['rhythm']['onset_rate']
            rhythm_beat_pos = data['rhythm']['beats_position']
            rhythm_beats_loudness_var = data['rhythm']['beats_loudness']['var']
            rhythm_danceability = data['rhythm']['danceability']

            tonal_chords_key = data['tonal']['chords_key'] # dynamic chord progression <---- map --> scale 
                                                           # || pitch|bass chroma 4accuracy
            tonal_chords_scale = data['tonal']['chords_scale'] 
            tonal_tuning_freq = data['tonal']['tuning_frequency'] 

            print ("Avg Loudness: " + str(avg_loudness) + " High: " + str(spec_energy_high) + " Low: " + str(spec_energy_low))
            print ("Rhythm BPM: " + str(rhythm_bpm))
            print ("Onset Rate: " + str(rhythm_onsetrate) + " Beat Position: " + str(rhythm_beat_pos))
            print ("Beat Loudness Var: " + str(rhythm_beats_loudness_var))
            print ("Danceability: " + str(rhythm_danceability))

            # rhythm_beat_pos # substract: delay timing avg --> servo sweep

            print ("Chord: " + str(tonal_chords_key) + " " + str(tonal_chords_scale))
            print ("Tuning Freq: " + str(tonal_tuning_freq))
         
        except yaml.YAMLError as e:
            print(e)

def SignalExit(signal, frame):
    os.system("rm -f *.wav *.yaml *.npy")
    sys.exit(0)

def CaptureHandler():
    CaptureLoad()

    if (EstimatedB() == -1):
      print '(Silent)'
      return -1

def ProcessHandler():
    EstimateTempo()
    EssentiaMusicExtractor()

    try:
      print '-- Playback --'
      ParseYAML('playback.yaml')
      print '-- Guitar --'
      ParseYAML('guitar.yaml')
    except:
      pass

    DetectGenre() 

    # todo:
    # genre -> prob - gradient -> tone suggestion
    # amp manual preselect

    '''
    # yaml/json parser -- essentia + curve fitting 
    print '[EQ balancer: ---(todo)]'
    print '[Dist/Delay/Reverb balancer: ---(todo)]'

    print '[Tuning: ---(yin pitch <-> current chord iff heavy||tdkAkur -> pisah)]'

    # direct / arduino ?
    print 'Arduino [servo]: ---(usb/firewire/thunderbold spec-boundless)'
    '''

    ## todo: recall db compare

    ## todo: auto song change - clear array, instead of counter
    ## yaml audio features - compare
    DetectPlaybackChange()

if __name__ == "__main__":

    Initialize()

    while (tidakPuas):
        if (CaptureHandler() == -1):
            continue

        ProcessHandler()

        # loop till OK
   
####
##
## zGPL
##
## bla bla bla bla
## bla bla bla bla
## 
## fuck the licensing system
## do what the fuck u want wiv it, claim it sell it /etc
##
####
