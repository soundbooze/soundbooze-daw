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

    client = jack.Client('interval-icish')

    regexPort = client.get_ports('(Calf Studio Gear:Analyzer|Calf Studio Gear:Equalizer 8 Band)')
    if (regexPort):

        try:
            if (sys.argv[1] == "playback"):
                client.connect(MONITOR1, 'Calf Studio Gear:Analyzer In #1')
                client.connect(MONITOR2, 'Calf Studio Gear:Analyzer In #2')
            elif (sys.argv[1] == "capture"):
                client.connect(CAPTURE1, 'Calf Studio Gear:Analyzer In #1')
                client.connect(CAPTURE2, 'Calf Studio Gear:Analyzer In #2')
            elif (sys.argv[1] == "pulseaudio"):
                client.disconnect(PULSEAUDIO1, PLAYBACK1)
                client.disconnect(PULSEAUDIO2, PLAYBACK2)
                client.connect(PULSEAUDIO1, 'Calf Studio Gear:Equalizer 8 Band In #1')
                client.connect(PULSEAUDIO2, 'Calf Studio Gear:Equalizer 8 Band In #2')
                client.connect('Calf Studio Gear:Equalizer 8 Band Out #1', PLAYBACK1)
                client.connect('Calf Studio Gear:Equalizer 8 Band Out #2', PLAYBACK2)

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
