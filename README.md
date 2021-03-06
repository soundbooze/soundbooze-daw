
![alt text](https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/photo.jpg "Home")
 
 # Device Setup

![alt text](https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/profile/user/bingung-not.png "Home")

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

### stability test / benchmark

- kernelshark
- ftrace, perf
- iperf (daw , netjack cluster)

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
- MINIMALIST / non-redudancy
- arduino sync
- jackd session port - reconnect on spof
- load-sharing

# Links

- https://wiki.debian.org/DebianInstaller/Modify/CD

# Guitar Tone (Sample Demos)

- https://www.youtube.com/watch?v=LlPdTQrzgtM
- https://www.youtube.com/watch?v=3jnhb_x3BAU
- https://www.youtube.com/watch?v=1W0NbsuI-j4
- https://www.youtube.com/watch?v=sI1xHw-FXQM
- https://www.youtube.com/watch?v=hCpUw_uZlzM

