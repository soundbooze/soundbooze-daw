```
# hciconfig
```

```
# hcitool -i hci1 scan
```

```
# bluetoothctl
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# default-agent
[bluetooth]# scan on

pair 00:1D:43:6D:03:26
connect 00:1D:43:6D:03:26
```

- https://github.com/ev3dev/ev3dev.github.io/pull/24/files/50787e9fae767f4a8e5e1748c5bb70b40eb9f259?short_path=2545682
- https://wiki.archlinux.org/index.php/Bluetooth_headset
