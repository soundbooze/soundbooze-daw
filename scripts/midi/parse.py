import sys
from mido import Message, MidiFile, MidiTrack

def ParseMIDI(filename):
    mid1 = MidiFile(filename)
    for i, track in enumerate(mid1.tracks):
            for msg in track:
                if not msg.is_meta:
                    s = str(msg).split(" ")
                    time = str(s[4]).split("=")
                    time = int(time[1])
                    try :
                        m = Message.from_bytes(msg.bytes())
                        print(m.note, m.velocity, time)
                    except:
                        pass

ParseMIDI("a.mid")
