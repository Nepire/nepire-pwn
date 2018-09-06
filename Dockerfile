FROM ubuntu:16.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get install libc6-dbg xinetd build-essential
RUN apt-get update && apt-get install -y lib32z1 xinetd build-essential
RUN apt-get update && apt-get install -y gcc-multilib xinetd build-essential
RUN apt-get update && apt-get install -y python-pip xinetd build-essential
RUN apt-get update && pip install pwntools
RUN apt-get update && apt-get install -y gdb xinetd build-essential
RUN apt-get update && apt-get install -y git xinetd build-essential
RUN git clone https://github.com/longld/peda.git ~/peda
RUN apt-get install wget
RUN wget -q -O ~/.gdbinit-gef.py https://github.com/hugsy/gef/raw/master/gef.py
RUN echo "source ~/peda/peda.py" >> ~/.gdbinit

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /lib* /home/ctf
RUN cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev
RUN mknod /home/ctf/dev/null c 1 3
RUN mknod /home/ctf/dev/zero c 1 5
RUN mknod /home/ctf/dev/random c 1 8
RUN mknod /home/ctf/dev/urandom c 1 9
RUN chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin
RUN cp /bin/sh /home/ctf/bin
RUN cp /bin/ls /home/ctf/bin
RUN cp /bin/cat /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail


COPY ./bin/ /home/ctf/
RUN chown -R root:ctf /home/ctf
RUN chmod -R 750 /home/ctf

CMD exec /bin/bash -c "/etc/init.d/xinetd start; trap : TERM INT; sleep infinity & wait"

EXPOSE 10000
