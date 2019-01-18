**manually build
```
apt-get install jackd2 pulseaudio qjackctl pulseaudio-module-jack jack-capture
```

# APT INSTALL

```
apt-get install audacity ardour 
apt-get install guitarix rakarrack 
apt-get install polyphone
apt-get install x42-plugins [multimedia-audio-plugins ***crash] 
apt-get install wah-plugins rev-plugins ste-plugins
apt-get install mda-lv2
apt-get install eq10q
# apt-get install calf-plugins
apt-get install tuxguitar 
# apt-get install jamin sweep 
apt-get install drumkv1-lv2 
apt-get install giada
apt-get install qjackctl a2jmidid qmidinet
apt-get install sonic-visualiser 
apt-get install mustang-plug wmaker
```

# Host

```
apt-get install jalv
apt-get lilv-utils  <--- lv2ls
```

# Video

```
apt-get install vlc simplescreenrecorder
apt-get install vlc-plugin-jack
apt-get install openshot lives krita
```

# Faust

```
apt-get install faust faustworks
```

# Polyphone

```
libstk0-dev 

https://www.polyphone-soundfonts.com/en/download
```

# Rubberband

```
apt-get install rubberband-cli rubberband-vamp rubberband-ladspa vocproc
```

# MIDI synth host

```
apt-get install qsynth bristol 
apt-get install qsampler
apt-get install jack-keyboard

apt-get install cecilia
apt-get install csound python-pyo
apt-get install aeolus synthv1 hexter qsynth ams
```

### lightweight (ideal for PI)

```
apt-get install amsynth zynaddsubfx
apt-get install fluidsynth sooperlooper qtractor
```

# MIDI Parser

```
apt-get install kmidimon midicsv
```

https://www.midieditor.org/

# Drum & Metronome

```
apt-get install drumgizmo
apt-get install hydrogen gtklick
apt-get install tk707
```

- https://groovemonkee.com/pages/free-midi-loops

# Soundfont

```
apt search soundfont
```

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
apt-get install oxygencursors thunar
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
