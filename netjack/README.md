### Master

##### Multicast

```
route add -net 224.0.0.0 netmask 240.0.0.0 dev enp2s0f0
ip maddr show
```

```
jackd
jack_load netmanager
jack_connect .. ...
```

### Slave

```
route add -net 224.0.0.0 netmask 240.0.0.0 dev enp8s0
ip maddr show
```

##### Multicast

```
jackd -R -d net -l 0
jack_load netadapter
jack_load audioadapter
jack_connect ... ...
```
### ALSA index

##### /etc/modprobe.d/...conf

```
options snd_usb_audio index=0
```
