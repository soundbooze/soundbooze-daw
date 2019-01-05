#!/usr/bin/env python

import sys
import socket, time
import subprocess as sp

# get mod-host pid
pid = sp.check_output("pgrep mod-host; exit 0", shell=True)
if pid == '':
    print 'mod-host is not running'
    exit(0)

# setup socket
s = socket.socket()
s.connect(('127.0.0.1', 5555))
s.settimeout(5)

def check_mod_host():
    if sp.check_output("pgrep mod-host; exit 0", shell=True) != pid:
        print 'mod-host died'
        exit(1)

def send_command(command):
    s.send(command)
    print 'sent:', command
    check_mod_host()

    try:
        resp = s.recv(1024)
        if resp: print 'resp:', resp
        return True

    except Exception:
        return False

#send_command('add http://calf.sourceforge.net/plugins/VintageDelay 0')

bpm = float(sys.argv[1]) / 2.0

send_command('param_set 0 bpm_host %f' % bpm)
send_command('param_set 0 bpm %f' % bpm)
send_command('param_set 0 mix_mode 0')

#send_command('remove 0')
