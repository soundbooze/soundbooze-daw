### Pre Install

```
dd if=debian-10.3.0-amd64-netinst.iso of=/dev/sdc bs=4M; sync
```

```
[ctrl-alt-f2] <>
mount -t iso9660 /dev/sdb1 /cdrom
mkdir /firmware
mount /dev/sdd /mnt && mount /dev/sdd1 /mnt
cp /mnt/firmware-iwlwifi.deb /firmware
```

### Wifi

```
wpa_supplicant -Dnl80211 -B -c ./key -iwlp1s0
dhclient wlp1s0
```

- https://wiki.debian.org/SourcesList

### Tools

```
apt-get -y install linux-image-rt-amd64
apt-get -y install dnsutils psutils tree vim vim-gui-common mlocate net-tools git
apt-get -y install curl lynx
```

### X11

```
apt-get -y install xorg wmaker chromium gimp
apt-get -y install firefox-esr task-gnome-desktop
```

### Audio

```
apt-get -y install jackd2 qjackctl jack-capture pulseaudio pulseaudio-module-jack alsa-utils dbus-x11
```

### Post

```
systemctl disable cron
systemctl disable rsyslog

/etc/systemd/logind.conf NAutoVTs
```

### Force jackd to start

- https://github.com/soundbooze/soundbooze-daw/tree/master/profile/user/pulse

```
$ /usr/bin/jackd -p128 -t10000 -dalsa -r48000 -p512 -n2 -m -D -C hw:USB -P hw:USB
$ pactl load-module module-jack-sink channels=2
$ pactl load-module module-jack-source channels=2
$ pactl set-default-sink jack_out
$ pactl set-default-source jack_in
```


### Jackd Pulseaudio Routing

# List play device

```
pacmd list-sinks | grep -e 'name:' -e 'index:'
```
  
# List record device

```
pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'
```
