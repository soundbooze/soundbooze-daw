import numpy as np
import cv2
from skimage import util, filters

import socket, time
import subprocess as sp

def __threshold_moving(input, last_image):
        if (last_image.shape == input.shape):
            output =  cv2.absdiff(input, last_image)
        else:
            output = numpy.ndarray(shape=input.shape, dtype=input.dtype)
        return input, output

cap = cv2.VideoCapture(1)
ret,old_frame = cap.read()

old_frame_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
old_sobel = util.invert(old_frame_gray)

# mod-host

def check_mod_host():
    if sp.check_output("pgrep mod-host; exit 0", shell=True) != pid:
        print 'mod-host died'
        exit(1)

def send_command(command):
    s.send(command)
    check_mod_host()

    try:
        resp = s.recv(1024)
        if resp:
            return True

    except Exception:
        return False

pid = sp.check_output("pgrep mod-host; exit 0", shell=True)
if pid == '':
    print 'mod-host is not running'
    exit(0)

s = socket.socket()
s.connect(('localhost', 5150))
s.settimeout(2)

send_command('add http://guitarix.sourceforge.net/plugins/gx_colwah_#_colwah_ 0')
send_command('connect system:capture_1 effect_0:in')
send_command('connect system:capture_2 effect_0:in')
send_command('connect effect_0:out system:playback_1')
send_command('connect effect_0:out system:playback_2')

while(1):

    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobel = util.invert(frame_gray)

    m = __threshold_moving(old_sobel, sobel)

    # naive - TODO: - movement <-- valChange
    #               - rnd var / ...process ? hmm, .. /stat inf
    #               - tap to enable/disable

    i, o = m


    # pedal

    sum_nd = np.sum(o)/750000

    v = np.round(sum_nd/100, 4)

    if (v > 1): 
        v = 1

    elif (v < 0):
        v = 0
       
    # print v

    '''
    value_min = 0.0
    value_max = 1.0
    '''

    send_command('param_set 0 WAH %f' % v)

    # pedal

    #print np.cumsum(oo)
    #oo = np.resize(o, (10, 10))
    #print oo.shape, oo.size
    #print  np.std(oo, axis=0)
    #print  np.sum(np.var(oo, axis=0))
    #print np.cumprod(oo)
    # naive


    #cv2.imshow('frame', sobel)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    old_gray = frame_gray.copy()

cv2.destroyAllWindows()
cap.release()

send_command('remove 0')
