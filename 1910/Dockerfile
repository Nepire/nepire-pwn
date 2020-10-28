FROM ubuntu:19.10
RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade tzdata
RUN apt-get update && apt-get install -y gdb gdb-multiarch vim git python3-pip python-setuptools python3-setuptools wget sudo
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install pwntools
RUN wget -q -O- https://raw.githubusercontent.com/Nepire/Pwngdb/master/install.sh | sh
