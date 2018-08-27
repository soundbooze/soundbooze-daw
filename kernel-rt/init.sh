#!/bin/sh

wget https://mirrors.edge.kernel.org/pub/linux/kernel/v4.x/linux-4.9.115.tar.xz
wget https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/4.9/patch-4.9.115-rt93.patch.xz

xz -cd linux-4.9.115.tar.xz | tar xvf -
cd linux-4.9.115
xzcat ../patch-4.9.115-rt93.patch.xz | patch -p1
