import mido as m

b = m.bpm2tempo(90)
t = m.tempo2bpm(444444)
t2 = m.tick2second(1, 96, 120)
s2 = m.second2tick(1.25e-06, 96, 120)
print t2 * 1000000 #ms
print s2
