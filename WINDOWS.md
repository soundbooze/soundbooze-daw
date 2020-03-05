# LESS PRIORITY

- https://wiki.debian.org/Wine

```
winecfg (Windows 10)
```

### netjack

- vst3 wine (carla)
- http://www.hermannseib.com/english/vsthost.htm
- https://www.powerdrumkit.com/

- [x] EZDrummer 2
- [x] FabFilter
- [x] FL Studio 20.

## Upgrade

```
sudo dpkg --add-architecture i386 
wget -qO - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -

sudo apt-add-repository https://dl.winehq.org/wine-builds/debian/

sudo apt-get update
sudo apt-get install --install-recommends winehq-stable

export PATH=$PATH:/opt/wine-stable/bin

wine --version 

wine-5.0
```
