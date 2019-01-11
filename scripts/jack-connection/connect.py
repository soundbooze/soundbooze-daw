import jack

STEREO_WIDTH_IN_L =  "Stereo width:In L"
STEREO_WIDTH_IN_R =  "Stereo width:In R"
STEREO_WIDTH_OUT_L = "Stereo width:Out L"
STEREO_WIDTH_OUT_R = "Stereo width:Out R"

TAP_DYNAMICS_IN_L =  "TAP Dynamics (St):Input Left"
TAP_DYNAMICS_IN_R =  "TAP Dynamics (St):Input Right"
TAP_DYNAMICS_OUT_L = "TAP Dynamics (St):Output Left"
TAP_DYNAMICS_OUT_R = "TAP Dynamics (St):Output Right"

TAP_TUBEWARMTH_IN =  "TAP TubeWarmth:Input"
TAP_TUBEWARMTH_OUT = "TAP TubeWarmth:Output"

client = jack.Client('GuitarTube')

#print client.get_ports()

client.connect(TAP_TUBEWARMTH_OUT, TAP_DYNAMICS_IN_L)
client.connect(TAP_TUBEWARMTH_OUT, TAP_DYNAMICS_IN_R)

client.connect(TAP_DYNAMICS_OUT_L, STEREO_WIDTH_IN_L)
client.connect(TAP_DYNAMICS_OUT_R, STEREO_WIDTH_IN_R)

client.connect(STEREO_WIDTH_OUT_L, 'system:playback_1')
client.connect(STEREO_WIDTH_OUT_R, 'system:playback_2')
