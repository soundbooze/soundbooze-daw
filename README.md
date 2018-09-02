# Device Setup

![alt text](https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/bingung-not.png "Home")

```
JACK
2 [Amplifier      ]: USB-Audio - Mustang Amplifier

- https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/soundcard.jpg

ALSA (additional USB guitar cable)
3 [Device         ]: USB-Audio - USB PnP Sound Device

- https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/guitar.jpg

Note: For reference, ALSA stores its settings in /var/lib/alsa/asound.state
```

#### ALSA non-pulseaudio (default direct devices)

- Minimal glitches/clicking/popping
- Recoding focus

```
more .asoundrc 
pcm.!default {
    type hw
    card 1
}

ctl.!default {
    type hw
    card 2
}
```

> ** qjackctl - Force 16 bit

#### Pulseaudio JACKD *overload

- overload
- good for web audio/desktop screen recording/plugin devel - testing/connection shared-buffer

```
Excessive CPU usage and distortion
Add a line to /etc/pulse/default.pa

load-module module-udev-detect tsched = 0
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
-

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

# Packages Installation

- https://github.com/soundbooze/soundbooze-daw/blob/master/PACKAGES.md

# TARGETs / AIMs

- STABility
- PERFormance
- minimise playBack clicks/pops
- raspberry PI preselected 
- arduino sync

# Tips

- Ardour: 
 
 - ardour: minmise plugins
 - pre-processed effect via audacity
 
- Guitarix:
 
 minimise convolution

- Synth / CAlf

  via standalone -> record -> wav <-- import to ardour ||
                                  <-- manual track / bus route
 - hydrogen / calf / plugins
 
  via standalone -> record -> wav <-- import to ardour
  
 - Desktop (lightweight) i.e: wmaker

# Links

- https://github.com/soundbooze/soundbooze-daw/blob/master/LINKS.md

# Sample Demos

- https://www.youtube.com/watch?v=3jnhb_x3BAU
- https://www.youtube.com/watch?v=1W0NbsuI-j4
- https://www.youtube.com/watch?v=CIo2e81qDI4
- https://www.youtube.com/watch?v=sI1xHw-FXQM
- https://www.youtube.com/watch?v=hCpUw_uZlzM

