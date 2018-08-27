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
make -j4 bzImage
make -j4 modules
make modules_install
make install

## update-initramfs -k 4.9.115-rt93 -u
/usr/sbin/update-grub2 -> update-grub
```

## Disable unused modules / drivers

- disable all network devices -> except UNIX_SOCKET (*)
- disable unused filesystems -> except ext2(M) ext4 -- CRC32(*)
- disable debug/tracer/profiler
- disable virtualization

## Priority

- https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/

## Test

- https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/worstcaselatency

