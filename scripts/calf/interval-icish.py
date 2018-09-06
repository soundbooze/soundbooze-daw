from subprocess import check_output
import sys
import time
import signal
import jack

CALFJACKHOST = 'calfjackhost'

def get_pid(name):
    try:
        return check_output(["pidof",name])
    except:
        pass

'''
def SignalExit(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, SignalExit)
'''

def ConnectJack():

    MONITOR1 = 'system:monitor_1'
    MONITOR2 = 'system:monitor_2'
    CAPTURE1 = 'system:capture_1'
    CAPTURE2 = 'system:capture_2'
    PLAYBACK1 = 'system:playback_1'
    PLAYBACK2 = 'system:playback_2'
    PULSEAUDIO1 = 'PulseAudio JACK Sink:front-left'
    PULSEAUDIO2 = 'PulseAudio JACK Sink:front-right'
    HYDROGEN1 = 'Hydrogen:out_L'
    HYDROGEN2 = 'Hydrogen:out_R'

    IN1 = "In #1"
    IN2 = "In #2"
    OUT1 = "Out #1"
    OUT2 = "Out #2"
    CALF_ANALYZER = "Calf Studio Gear:Analyzer"
    CALF_8BAND_EQUALIZER = "Calf Studio Gear:Equalizer 8 Band"
    CALF_MULTIBAND_COMPRESSOR = "Calf Studio Gear:Multiband Compressor"
    CALF_MULTIBAND_LIMITER = "Calf Studio Gear:Multiband Limiter"
    CALF_REVERB = "Calf Studio Gear:Reverb"

    client = jack.Client('interval-icish')

    regexPort = client.get_ports('(Calf Studio Gear:Analyzer|Calf Studio Gear:Equalizer 8 Band|Calf Studio Gear:Multiband Compressor|Calf Studio Gear:Multiband Limiter)')
    if (regexPort):

        try:
            if (sys.argv[1] == "playback"):
                client.connect(MONITOR1, CALF_ANALYZER + " " + IN1)
                client.connect(MONITOR2, CALF_ANALYZER + " " + IN2)
            elif (sys.argv[1] == "capture"):
                client.connect(CAPTURE1, CALF_ANALYZER + " " + IN1)
                client.connect(CAPTURE2, CALF_ANALYZER + " " + IN2)
            elif (sys.argv[1] == "pulseaudio"):
                client.disconnect(PULSEAUDIO1, PLAYBACK1)
                client.disconnect(PULSEAUDIO2, PLAYBACK2)
                client.connect(PULSEAUDIO1, CALF_8BAND_EQUALIZER + " " + IN1)
                client.connect(PULSEAUDIO2, CALF_8BAND_EQUALIZER + " " + IN2)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT1, PLAYBACK1)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT2, PLAYBACK2)
            elif (sys.argv[1] == "hydrogen"):
                client.disconnect(HYDROGEN1, PLAYBACK1)
                client.disconnect(HYDROGEN2, PLAYBACK2)
                client.connect(HYDROGEN1, CALF_MULTIBAND_COMPRESSOR + " " + IN1)
                client.connect(HYDROGEN2, CALF_MULTIBAND_COMPRESSOR + " " + IN2)
                client.connect(CALF_MULTIBAND_COMPRESSOR + " " + OUT1, CALF_MULTIBAND_LIMITER + " " + IN1)
                client.connect(CALF_MULTIBAND_COMPRESSOR + " " + OUT2, CALF_MULTIBAND_LIMITER + " " + IN2)
                client.connect(CALF_MULTIBAND_LIMITER + " " + OUT1, CALF_REVERB + " " + IN1)
                client.connect(CALF_MULTIBAND_LIMITER + " " + OUT2, CALF_REVERB + " " + IN2)
                client.connect(CALF_REVERB + " " + OUT1, PLAYBACK1)
                client.connect(CALF_REVERB + " " + OUT2, PLAYBACK2)

        except:
            pass

        return True

    client.deactivate()
    client.close()

    return False

while (True):

    r = get_pid(CALFJACKHOST)
    if (r != None):
        if (ConnectJack()):
            sys.exit(0)

    time.sleep(1)

client = None
