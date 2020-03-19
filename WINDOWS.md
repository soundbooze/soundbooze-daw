# LESS PRIORITY

- https://wiki.debian.org/Wine

```
winecfg (Windows 10)
```

## Upgrade 5.0

```
dpkg --add-architecture i386 
wget -qO - https://dl.winehq.org/wine-builds/winehq.key | apt-key add -

apt-add-repository https://dl.winehq.org/wine-builds/debian/

apt-get update
apt-get install --install-recommends winehq-stable

export PATH=$PATH:/opt/wine-stable/bin

```

### Tested

- vst3 wine (carla)

- [x] EZDrummer 2
- [x] FabFilter
- [x] FL Studio 20.
- [x] MT Power Drumkit
