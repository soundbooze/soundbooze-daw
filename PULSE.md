```
dbus-x11
run jackd

pactl load-module module-jack-sink channels=2
pactl load-module module-jack-source channels=2
pactl set-default-sink jack_out
pactl set-default-source jack_in
```
