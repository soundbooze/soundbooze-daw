# LESS PRIORITY

- https://wiki.debian.org/Wine
- https://wiki.winehq.org/Debian

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
## Upgrade 5.4

```
apt install --install-recommends winehq-staging
```
