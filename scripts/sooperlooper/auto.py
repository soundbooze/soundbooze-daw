import time
import rtmidi

midiout = rtmidi.MidiOut()
midiout.open_port(0)

def RecordToggle():

    note_on = [0x90, 60, 115]
    note_off = [0x80, 60, 0]
    midiout.send_message(note_on)

    time.sleep(0.2)

    midiout.send_message(note_off)

    time.sleep(2)

while(True):
    RecordToggle()


del midiout
