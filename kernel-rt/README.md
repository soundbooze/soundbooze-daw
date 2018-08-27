# RT Linux (pre-compiled)

```
apt-get install linux-image-rt-amd64 
apt-get install htop
```

### manual kernel build (patch+reqs)

```
 apt-get install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex libelf-dev bison
```

> init.sh

```
make menuconfig
make bzImage
make modules_install
make install
```

## Priority

- https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/

## Disable unused modules / drivers

- disable all network devices
- disable unused filesystems
- disable debug/tracer/profiler
- disable virtualization
