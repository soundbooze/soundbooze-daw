### Pre Install

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

### Tools

```
apt-get -y install linux-image-rt-amd64
apt-get -y install dnsutils psutils tree vim vim-gui-common mlocate net-tools
apt-get -y install curl lynx wget
apt-get -y install xorg wmaker firefox-esr chromium task-gnome-desktop gimp
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
