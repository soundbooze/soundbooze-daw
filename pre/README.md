### Pre Install

```
dd if=debian-10.3.0-amd64-netinst.iso of=/dev/sdc bs=4M; sync
```

```
[ctrl-alt-f2] <>
mount -t iso9660 /dev/sdb1 /cdrom
mkdir /firmware
(mount /dev/sdd /mnt) && mount -t ext4 /dev/sdd1 /mnt
cp /mnt/firmware-iwlwifi.deb /firmware
```

### Temperature

```
 apt-get -y install lm-sensors
 # sensors
```

```
 apt-get -y install hddtemp
 # hddtemp /dev/sda
```

### Battery

```
 apt-get -y install acpitool
 # acpitool
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
apt-get -y install dnsutils psutils tree psmisc vim vim-gui-common mlocate net-tools git 
apt-get -y install build-essential autoconf automake libtool
apt-get -y install software-properties-common apt-transport-https
apt-get -y install curl lynx procinfo sysstat htop
apt-get -y install cscope ctags cflow strace lsod
```

### X11

```
apt-get -y install xorg xorg-dev wmaker chromium firefox-esr gimp dbus-x11
```

### Audio

```
apt-get -y install jackd2 qjackctl jack-capture pulseaudio pulseaudio-module-jack
apt-get -y install alsa-utils
apt-get -y install zita-resampler zita-rev1 libzita-convolver-dev libzita-resampler-dev libzita-convolver3
```

### Post

```
systemctl disable cron
systemctl disable rsyslog
systemctl disable polkit
systemctl disable minissdpd
 
/etc/systemd/logind.conf ReserveVT=2
```

### Jackd Pulseaudio Routing

- https://github.com/soundbooze/soundbooze-daw/tree/master/profile/user/pulse

```
$ /usr/bin/jackd -p128 -t10000 -dalsa -r48000 -p512 -n2 -m -D -C hw:USB -P hw:USB
$ pactl load-module module-jack-sink channels=2
$ pactl load-module module-jack-source channels=2
$ pactl set-default-sink jack_out
$ pactl set-default-source jack_in
```

#### List play device

```
pacmd list-sinks | grep -e 'name:' -e 'index:'
```
  
#### List record device

```
pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'
```
