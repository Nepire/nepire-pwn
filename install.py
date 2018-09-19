import os

def build_images():
	os.system('docker build -t pwn ~/nepire-pwn/')
	os.system('docker run --cap-add=SYS_PTRACE -dit --name nepire-pwn pwn')
	#build images

def create_bin():
	os.system('touch ~/nepire-pwn/nepire-pwn')

	os.system('echo "#! /bin/bash" > ~/nepire-pwn/nepire-pwn')
	os.system('echo "#Author=Ep3ius_nepire" >> ~/nepire-pwn/nepire-pwn')
	os.system('echo "docker cp ~/nepire-pwn/process/ nepire-pwn:/home/ctf/" >> ~/nepire-pwn/nepire-pwn')
	os.system('echo "docker exec -it nepire-pwn /bin/zsh" >> ~/nepire-pwn/nepire-pwn')

	os.system('chmod 777 ~/nepire-pwn/nepire-pwn')
	os.system('cp ~/nepire-pwn/nepire-pwn /usr/bin/nepire-pwn')

def nepire_pwn():
	over = '''
			 _   _ _____ ____ ___ ____  _____                          
			| \ | | ____|  _ \_ _|  _ \| ____|     _ ____      ___ __  
			|  \| |  _| | |_) | || |_) |  _| _____| '_ \ \ /\ / / '_ \ 
			| |\  | |___|  __/| ||  _ <| |__|_____| |_) \ V  V /| | | |
			|_| \_|_____|_|  |___|_| \_\_____|    | .__/ \_/\_/ |_| |_|
			                                      |_|                  
	'''
	print over

def version():
	version = '1.0'

	print version

def upload_process():
	os.system('docker cp ~/nepire-pwn/process/ nepire-pwn:/home/ctf/')

def main():
	build_images()
	upload_process()
	create_bin()
	version()
	nepire_pwn()


if __name__ == "__main__":
    main()


