(room-level accuracy - use @your own risk)

# Device Setup

![alt text](https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/bingung-not.png "Home")

<b>Frames/Period : 256</b>

```
JACK

0 [Track          ]: USB-Audio - M-Audio Fast Track

1 [Amplifier      ]: USB-Audio - Mustang Amplifier

- https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/soundcard.jpg

ALSA (additional USB guitar cable)

2 [Device         ]: USB-Audio - USB PnP Sound Device

- https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/guitar.jpg

Note: For reference, ALSA stores its settings in /var/lib/alsa/asound.state
```

<pre>
# play device

pacmd list-sinks | grep -e 'name:' -e 'index:'
pacmd set-default-sink 1 

# record device

pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'
pacmd set-default-source 4

## audacity - custom hw: / [jack]

## jamin : app -> qjackctl -> jamin -> speakerOut

## ardour [jack]
</pre>

- https://github.com/jackaudio/jackaudio.github.com/wiki/WalkThrough_User_PulseOnJack
- https://linux.die.net/man/5/pulse-daemon.conf
- https://wiki.linuxaudio.org/wiki/system_configuration
-

### known problems:

- https://www.kernel.org/doc/html/v4.17/sound/soc/pops-clicks.html
- jack-pulse :audio clicking
- drumgizmo xml / wav load
- simplescreenrecorder cpu load 
- libvamp_essentia.so .. crashed

### stability test / benchmark

- kernelshark
- ftrace, perf
- system-wide - apps -... -> pi

## Connections

<pre>
> Setup: [Audio - Jack] [Soundfont: select] [Enable MIDI Input: Jack]
>
> Jack connection [Audio]: 
> zynaddsubfx -> system
>
> Jack connection [MIDI]: 
> jack-keyboard -> qsynth 
> jack-keyboard_midi_out -> zynaddsubfx_midi_input

<b>Ardour: </b>
  - MIDI connection: 
  
  IN: [Source: Other] - [Destination: Ardour Tracks]
  OUT: [Source: Ardour Tracks] - [Destination: Other]
  
  > Jack connection [Audio]: 
  > zynaddsubfx -> ardour
  
  [jack-keyboard - appPanel]
  Connected to : ardourMIDI -> midi_in

</pre>

# TARGETs / AIMs

- STABility
- PERFormance
- minimise playBack clicks/pops
- raspberry PI preselected 
- MINIMALIST / non-redudancy
- arduino sync / preselected apps
- jackd session port - reconnect on spof

# Packages Installation

- https://github.com/soundbooze/soundbooze-daw/blob/master/PACKAGES.md

# Links

- https://github.com/soundbooze/soundbooze-daw/blob/master/LINKS.md

# Sample Demos

- https://www.youtube.com/watch?v=3jnhb_x3BAU
- https://www.youtube.com/watch?v=1W0NbsuI-j4
- https://www.youtube.com/watch?v=sI1xHw-FXQM
- https://www.youtube.com/watch?v=hCpUw_uZlzM

