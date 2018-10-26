```
# apt-get install bluez-tools bluez
# apt-get install pulseaudio-module-bluetooth
# systemctl start bluetooth
```

### pulseaudio default.pa

```
load-module module-bluetooth-policy
load-module module-bluetooth-discover
```

### DBUS

```
# vim /etc/dbus-1/system.d/pulseaudio-system.conf

 <allow send_destination="org.bluez"/> 
```

### HCI Tool

```
# hciconfig
# hcitool -i hci1 scan

# hcitool info 00:11:11:28:07:01
# rfcomm bind /dev/rfcomm0 00:11:11:28:07:01
# rfcomm release 0

```

### CTL

```
# bluetoothctl

[bluetooth]# list
[bluetooth]# select 11:11:11:11:11:11
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# default-agent
[bluetooth]# scan on

[bluetooth]# pair 74:E5:43:B1:8D:95
[bluetooth]# trust 74:E5:43:B1:8D:95
[bluetooth]# connect 74:E5:43:B1:8D:95
```

### Config

```
# cat /etc/default/bluetooth

HID2HCI_ENABLED=1
HID2HCI_UNDO=1

```

- https://github.com/ev3dev/ev3dev.github.io/pull/24/files/50787e9fae767f4a8e5e1748c5bb70b40eb9f259?short_path=2545682

