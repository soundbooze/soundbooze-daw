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

/usr/sbin/update-grub2 -> update-grub
```

## Disable unused modules / drivers

- disable all network devices -> except UNIX_SOCKET (*)
- disable unused filesystems -> except ext2(M) ext4 -- CRC32(*)
- disable debug/tracer/profiler
- disable virtualization

> rmmod -f snd_hda_intel

## Priority

- https://taste.tuxfamily.org/wiki/index.php?title=Tricks_and_tools_for_PREEMPT-RT_kernel
- https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/

## Test

- https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/worstcaselatency

## /etc/sysctl.conf

```
vm.swappiness = 10
fs.inotify.max_user_watches = 524288
```

```
sysctl -w vm.swappiness=10
sysctl fs.inotify.max_user_watches=524288
echo 2048 > /sys/class/rtc/rtc0/max_user_freq
echo 2048 > /proc/sys/dev/hpet/max-user-freq
```

## DISK I/O Scheduler

- https://www.techrepublic.com/article/how-to-change-the-linux-io-scheduler-to-fit-your-needs/

## Blacklist

- cat /etc/modprobe.d/snd-hda-intel.conf 

```
blacklist snd_hda_intel
blacklist thunderbolt
blacklist firewire_ohci
blacklist firewire_core
blacklist btusb
blacklist pcspkr
blacklist ip_tables
```


