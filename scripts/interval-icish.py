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

    client = jack.Client('interval-icish')

    regexPort = client.get_ports('Calf Studio Gear:Analyzer')
    if (regexPort):
        print 'Connecting'
        client.connect(MONITOR1, 'Calf Studio Gear:Analyzer In #1')
        client.connect(MONITOR2, 'Calf Studio Gear:Analyzer In #2')
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
