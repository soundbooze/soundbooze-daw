import jack

client = jack.Client('dummy')
client.connect('fluidsynth:r_00', 'Calf Studio Gear:Multiband Compressor In #1')
client.connect('fluidsynth:l_00', 'Calf Studio Gear:Multiband Compressor In #2')
client.deactivate()
client.close()
