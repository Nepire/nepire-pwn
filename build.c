#include <stdio.h>
#include <stdlib.h>
int build_dockerfile()
{
	system("mkdir ~/nepire-pwn/");
	system("mkdir ~/nepire-pwn/process/");
	system("touch ~/nepire-pwn/Dockerfile");
	system("touch ~/nepire-pwn/Dockerfile");
}
int build_nepire_pwn()
{
	system('docker build -t pwn ~/nepire-pwn/');
	system('docker run -dit --name nepire-pwn pwn');
	del_dockerfile();
}
int del_dockerfile()
{
	system('rm ~/nepire-pwn/Dockerfile');
	
}
int yum_install_docker()
{
	system('yum install -y docker-ce');
}
int apt_install_docker()
{
	system('apt-get install -y docker.io');
}
int pacman_S_docker()
{
	system('pacman -S docker --noconfirm');
}
int cretae_bin()
{
	system('touch ~/nepire-pwn/nepire-pwn');
	system('touch ~/nepire-pwn/link-nepire-pwn');
	system('echo "docker cp ~/nepire-pwn/process nepire-pwn:/home/ctf/process" > ~/nepire-pwn/link-nepire-pwn');
	system('echo "docker exec -it nepire-pwn /usr/bin/fish" >> ~/nepire-pwn/link-nepire-pwn');
	system('echo "sh ~/nepire-pwn/link-nepire-pwn" > ~/nepire-pwn/nepire-pwn');
	system('chmod 777 ~/nepire-pwn/link-nepire-pwn');
	system('chmod 777 ~/nepire-pwn/nepire-pwn');
	system('cp ~/nepire-pwn/nepire-pwn /usr/bin/nepire-pwn');
}
int output()
{
	puts(" _   _ _____ ____ ___ ____  _____                          ");
	puts("| \\ | | ____|  _ \\_ _|  _ \\| ____|     _ ____      ___ __  ");
	puts("|  \\| |  _| | |_) | || |_) |  _| _____| '_ \\ \\ /\\ / / '_ \\ ");
	puts("| |\\  | |___|  __/| ||  _ <| |__|_____| |_) \\ V  V /| | | |");
	puts("|_| \\_|_____|_|  |___|_| \\_\\_____|    | .__/ \\_/\\_/ |_| |_|");
	puts("                                      |_|                  ");

}
int main()
{
	build_dockerfile();
	puts("SUCESS BUILD DOCKERFILE");
	puts("START BUILD NEPIRE-PWN");
	build_nepire_pwn();
	cretae_bin();
	puts("SUCESS BUILD NEPIRE-PWN");
	output();
	return 0;
}