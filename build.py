import os
os.system('docker build -t pwn .')
os.system('docker run -dit --name nepire-pwn pwn')
