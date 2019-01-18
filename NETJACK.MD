### Master

```
route add -net 224.0.0.0 netmask 240.0.0.0 dev if0
jackd
jack_load netmanager
```

### Slave

```
route add -net 224.0.0.0 netmask 240.0.0.0 dev if0
jackd -R -d net
jack_load netadapter
jack_load audioadapter
```
