import jack

client = jack.Client('test')
allPorts = client.get_ports()
#recdPort =client.get_ports(is_audio=True, is_output=True, is_physical=True)
#regexPort = client.get_ports('^[Cc]alf*')

for p in allPorts:
    print p

client.deactivate()
client.close()
