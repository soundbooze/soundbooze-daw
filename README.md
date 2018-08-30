# Device Setup

**manually build
```
apt-get install jackd2 pulseaudio qjackctl pulseaudio-module-jack jack-capture
```

![alt text](https://raw.githubusercontent.com/soundbooze/soundbooze-daw/master/bingung-not.png "Home")

```
JACK
2 [Amplifier      ]: USB-Audio - Mustang Amplifier

ALSA (additional USB guitar cable)
3 [Device         ]: USB-Audio - USB PnP Sound Device

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
- drumgizmo xml / way load
- simplescreenrecorder cpu load 
-

### stability test / benchmark

- kernelshark
- ftrace, perf
- system-wide - apps -... -> pi

# APT INSTALL

```
apt-get install audacity ardour 
apt-get install guitarix rakarrack 
apt-get install polyphone
apt-get install x42-plugins [multimedia-audio-plugins ***crash]
# apt-get install calf-plugins
apt-get install tuxguitar 
# apt-get install jamin sweep qtractor
apt-get install drumkv1-lv2
apt-get install qjackctl a2jmidid
apt-get install sonic-visualiser 
apt-get install mustang-plug wmaker
```

# Video

```
apt-get install vlc simplescreenrecorder
apt-get install vlc-plugin-jack
apt-get install openshot lives
```

# Faust

```
apt-get install faust faustworks
```

# Rubberband

```
apt-get install rubberband-cli rubberband-vamp rubberband-ladspa librubberband-dev
```

# MIDI synth host

```
apt-get install qsynth bristol
apt-get install fluidsynth libfluidsynth-dev 
apt-get install jack-keyboard

apt-get install cecilia
apt-get install csound sooperlooper python-pyo
apt-get install aeolus synthv1 hexter qsynth ams
```

### lightweight (ideal for pi)

```
apt-get install amsynth zynaddsubfx
```

# MIDI Parser

```
apt-get install kmidimon midicsv
```

# GIT synth, plugin etc/

- https://github.com/mtytel/helm
- https://github.com/brummer10/GxPlugins.lv2
- https://libremusicproduction.com/tools/lsp-plugins
- https://github.com/brummer10/GxVBassPreAmp.lv2
- https://github.com/ssj71/rkrlv2/tree/master/src
- https://padthv1.sourceforge.io/
-

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

# Drum & Metronome

```
apt-get install drumgizmo
apt-get install hydrogen gtklick
```

- https://groovemonkee.com/pages/free-midi-loops

# Soundfont

- https://x42-plugins.com/x42/x42-avldrums
- https://github.com/x42/avldrums.lv2
- https://www.polyphone-soundfonts.com/en/download

# Software & Updates -> mirror list

```
# cat /etc/apt/sources.list

...

deb http://http.debian.net/debian/ stretch main contrib non-free
deb http://ftp.debian.org/debian stretch-backports main
deb http://deb.opera.com/opera-stable/ stable non-free

# apt-get install opera-stable tilix

```

# Misc

```
apt-get install oxygencursors
```

## Unused

```
apt-get purge evolution
```

# GNOME

```
#cat .config/gtk-3.0/gtk.css 

headerbar.default-decoration {
  padding-top: 0px;
  padding-bottom: 0px;
  min-height: 0px;
  font-size: 1.1em;
}

headerbar.default-decoration button.titlebutton {
  padding: 0px;
  min-height: 0px;
}
```

## Disable Services

```
 systemctl disable polkit | iio-sensor-proxy | upower
 systemctl stop polkit | iio-sensor-proxy | upower
 ```
 
# FIRMWARE

```
b43-fwcutter
firmware-b43-installer
firmware-linux-free 
firmware-misc-nonfree
```

# TARGETs / AIMs

- STABility
- PERFormance
- minimise playBack clicks/pops

# Links

- https://github.com/soundbooze/soundbooze-daw/blob/master/LINKS.md
