import os

def build_images():
	os.system('docker build -t pwn ~/nepire-pwn/DOCKER/')
	os.system('docker run --cap-add=SYS_PTRACE -dit --name nepire-pwn pwn')
	#build images

def create_bin():
	add_process_permission = '''
	echo "docker exec nepire-pwn bash -c 'chmod -R u+x /home/ctf/* '" >> ~/nepire-pwn/nepire-pwn
    '''

	os.system('touch ~/nepire-pwn/nepire-pwn')

	os.system('echo "#! /bin/bash" > ~/nepire-pwn/nepire-pwn')
	os.system('echo "#Author=Ep3ius_nepire" >> ~/nepire-pwn/nepire-pwn')
	os.system('echo "docker cp ~/nepire-pwn/process/ nepire-pwn:/home/ctf/" >> ~/nepire-pwn/nepire-pwn')
	os.system(add_process_permission) #add permission u+x
	os.system('echo "docker exec -it nepire-pwn /usr/bin/fish" >> ~/nepire-pwn/nepire-pwn')

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
	version = '1.1'

	print version

def upload_process():
	os.system('docker cp ~/nepire-pwn/process/ nepire-pwn:/home/ctf/')

def stop_docker():
	os.system('docker stop nepire-pwn')

def upload_tools():
	#swich gdb-tools 
	os.system('')

def main():
	build_images()
	upload_process()
	create_bin()
	version()
	nepire_pwn()


if __name__ == "__main__":
    main()


