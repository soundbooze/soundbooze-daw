### References

- https://github.com/jackaudio/jackaudio.github.com/wiki/WalkThrough_User_PulseOnJack
- https://linux.die.net/man/5/pulse-daemon.conf
- https://wiki.linuxaudio.org/wiki/system_configuration
- https://wiki.linuxaudio.org/wiki/list_of_jack_frame_period_settings_ideal_for_usb_interface

### Device UUID

```
# blkid /dev/sdb1
```

### known problems:

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
