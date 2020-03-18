```
apt-get install dbus-x11

$ jackd -p512 -dalsa -r48000 -p512 -n2 -D -Chw:USB -Phw:USB 

$ pactl load-module module-jack-sink channels=2
$ pactl load-module module-jack-source channels=2
$ pactl set-default-sink jack_out
$ pactl set-default-source jack_in
```
