#! /bin/bash
#Author = Ep3ius_nepire
git clone https://github.com/Nepire/nepire-pwn.git ~/nepire-pwn/
cd ~/nepire-pwn
if ! [ -x "$(command -v docker)" ]; then
  sudo apt-get install docker.io
fi
chmod a+x ~/nepire-pwn/*
sudo python install.py
