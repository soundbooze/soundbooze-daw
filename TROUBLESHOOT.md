### Device UUID

```
# blkid /dev/sdb1
```
### Touchpad Libinput

```
apt remove xserver-xorg-input-synaptics
apt install xserver-xorg-input-libinput

 16 Section "InputClass"
 17         Identifier "libinput touchpad catchall"
 18         MatchIsTouchpad "on"
 19         MatchDevicePath "/dev/input/event*"
 20         Driver "libinput"
 21         Option "Tapping" "on"
 22 EndSection
```

### known problems:

Evolution

- https://askubuntu.com/questions/480753/remove-evolution-calendar-factory-from-startup

- https://www.kernel.org/doc/html/v4.17/sound/soc/pops-clicks.html
- libvamp_essentia.so .. crashed

(room-level accuracy - use @your own risk)

## ICONS

```
$HOME .local/share/applications

[Desktop Entry]
Name=sonic-visualiser
Comment=sonic-visualiser
GenericName=DAW
Type=Application
Categories=Music;X-Sound;Audio;
Keywords=music;;alsa;jack;realtime;standalone;lv2;
Exec=sonic-visualiser
TryExec=sonic-visualiser
Terminal=false
StartupNotify=true
Icon=/usr/local/share/pixmaps/sonic-visualser.png
```

### References

- https://github.com/jackaudio/jackaudio.github.com/wiki/WalkThrough_User_PulseOnJack
- https://linux.die.net/man/5/pulse-daemon.conf
- https://wiki.linuxaudio.org/wiki/system_configuration
- https://wiki.linuxaudio.org/wiki/list_of_jack_frame_period_settings_ideal_for_usb_interface
