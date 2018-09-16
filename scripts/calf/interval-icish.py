from subprocess import check_output
import jack

import os, sys, socket, signal, time

LOCALHOST = 'localhost'
CALFJACKHOST = 'calfjackhost'
MODHOST = 'mod-host'

modhost_plugins = [
            'http://calf.sourceforge.net/plugins/Analyzer',
            'http://calf.sourceforge.net/plugins/Equalizer8Band',
            'http://calf.sourceforge.net/plugins/MultibandCompressor',
            'http://calf.sourceforge.net/plugins/MultibandLimiter',
            'http://calf.sourceforge.net/plugins/Reverb'
          ]

# --------------- Modhost

def send_command(s, command):
    s.send(command)
    time.sleep(0.1)

    try:
        resp = s.recv(1024)
        return True

    except Exception:
        return False

def run_via_modhost():
    os.system(MODHOST + " -p 5150")

def modhost_add_plugins():
    time.sleep(0.5)
    s = socket.socket()
    s.connect((LOCALHOST, 5150))
    s.settimeout(5)

    for i, plugin in enumerate(modhost_plugins):
        send_command(s, 'add %s %i' % (plugin, i))

    s.close()

def modhost_remove_plugins():
    time.sleep(0.5)
    s = socket.socket()
    s.connect((LOCALHOST, 5150))
    s.settimeout(5)

    for i in range(len(modhost_plugins)):
        send_command(s, 'remove %i' % i)

    s.close()

def get_pid(name):
    try:
        return check_output(["pidof",name])
    except:
        pass

def ConnectSocket():
    run_via_modhost()
    modhost_add_plugins()

# --------------- Jack

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

    SOOPERLOOPER0_IN1 = 'sooperlooper:loop0_in_1'
    SOOPERLOOPER0_IN2 = 'sooperlooper:loop0_in_2'
    SOOPERLOOPER0_OUT1 = 'sooperlooper:loop0_out_1'
    SOOPERLOOPER0_OUT2 = 'sooperlooper:loop0_out_2'

    #SOOPERLOOPER1_IN1 = 'sooperlooper:loop1_in_1'
    #SOOPERLOOPER1_IN2 = 'sooperlooper:loop1_in_2'
    SOOPERLOOPER1_OUT1 = 'sooperlooper:loop1_out_1'
    SOOPERLOOPER1_OUT2 = 'sooperlooper:loop1_out_2'
    YOSHIMI_L = 'yoshimi:left'
    YOSHIMI_R = 'yoshimi:right'

    AMSYNTH_L = 'amsynth:L out'
    AMSYNTH_R = 'amsynth:R out'

    QSYNTH_L = 'qsynth:l_00'
    QSYNTH_R = 'qsynth:r_00'

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

    regexPort = client.get_ports('(' + CALF_ANALYZER + 
                                 '|' + CALF_8BAND_EQUALIZER + 
                                 '|' + CALF_MULTIBAND_COMPRESSOR +
                                 '|' + CALF_MULTIBAND_LIMITER + 
                                 '|' + 'sooperlooper' + 
                                 '|' + 'amsynth' + 
                                 '|' + 'yoshimi' + 
                                 '|' + 'qsynth)')

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
                client.connect(CALF_MULTIBAND_LIMITER + " " + OUT1, CALF_8BAND_EQUALIZER + " " + IN1)
                client.connect(CALF_MULTIBAND_LIMITER + " " + OUT2, CALF_8BAND_EQUALIZER + " " + IN2)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT1, CALF_REVERB + " " + IN1)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT2, CALF_REVERB + " " + IN2)
                client.connect(CALF_REVERB + " " + OUT1, PLAYBACK1)
                client.connect(CALF_REVERB + " " + OUT2, PLAYBACK2)
            elif (sys.argv[1] == "sooperlooper"):
                client.connect(CAPTURE1, SOOPERLOOPER0_IN1)
                client.connect(CAPTURE2, SOOPERLOOPER0_IN2)
                client.connect(SOOPERLOOPER0_OUT1, PLAYBACK1)
                client.connect(SOOPERLOOPER0_OUT2, PLAYBACK2)
                client.connect(SOOPERLOOPER1_OUT1, PLAYBACK1)
                client.connect(SOOPERLOOPER1_OUT2, PLAYBACK2)
            elif (sys.argv[1] == "yoshimi"):
                client.disconnect(YOSHIMI_L, PLAYBACK1)
                client.disconnect(YOSHIMI_R, PLAYBACK2)
                client.connect(YOSHIMI_L, CALF_8BAND_EQUALIZER + " " + IN1)
                client.connect(YOSHIMI_R, CALF_8BAND_EQUALIZER + " " + IN2)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT1, CALF_REVERB + " " + IN1)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT2, CALF_REVERB + " " + IN2)
                client.connect(CALF_REVERB + " " + OUT1, PLAYBACK1)
                client.connect(CALF_REVERB + " " + OUT2, PLAYBACK2)
            elif (sys.argv[1] == "amsynth"):
                client.disconnect(AMSYNTH_L, PLAYBACK1)
                client.disconnect(AMSYNTH_R, PLAYBACK2)
                client.connect(AMSYNTH_L, CALF_8BAND_EQUALIZER + " " + IN1)
                client.connect(AMSYNTH_R, CALF_8BAND_EQUALIZER + " " + IN2)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT1, CALF_REVERB + " " + IN1)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT2, CALF_REVERB + " " + IN2)
                client.connect(CALF_REVERB + " " + OUT1, PLAYBACK1)
                client.connect(CALF_REVERB + " " + OUT2, PLAYBACK2)
            elif (sys.argv[1] == "qsynth"):
                client.disconnect(QSYNTH_L, PLAYBACK1)
                client.disconnect(QSYNTH_R, PLAYBACK2)
                client.connect(QSYNTH_L, CALF_8BAND_EQUALIZER + " " + IN1)
                client.connect(QSYNTH_R, CALF_8BAND_EQUALIZER + " " + IN2)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT1, CALF_REVERB + " " + IN1)
                client.connect(CALF_8BAND_EQUALIZER + " " + OUT2, CALF_REVERB + " " + IN2)
                client.connect(CALF_REVERB + " " + OUT1, PLAYBACK1)
                client.connect(CALF_REVERB + " " + OUT2, PLAYBACK2)

        except:
            pass

        return True

    client.deactivate()
    client.close()

    return False

# --------------- Misc

def SignalExit(signal, frame):
    modhost_remove_plugins()
    sys.exit(0)

# --------------- Main

signal.signal(signal.SIGINT, SignalExit)

# ConnectSocket() -- TODO: map effects names

while (True):

    '''
    r = get_pid(CALFJACKHOST)
    if (r != None):
        if (ConnectJack()):
            sys.exit(0)
    '''

    if (ConnectJack()):
          sys.exit(0)

    time.sleep(1)

client = None
