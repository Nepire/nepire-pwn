# nepire-pwn
nepire的pwn解题环境

### 必要环境
docker、docker-compose

### 前置环境安装(ubuntu)
```
sudo apt-get install docker.io
sudo apt-get install python-pip
sudo pip install docker-compose
```
或者

``` 
sudo apt-get install docker.io
sudo curl -L https://github.com/docker/compose/releases/download/1.16.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose
```

#####测试安装结果
```
docker -h
docker-compose --version
```
### 工具目录
> 1.pwntools
>
> 2.gdb
>
> 3.peda、gef
>
> 4.vim
