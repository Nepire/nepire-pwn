FROM ubuntu:16.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get install libc6-dbg
RUN apt-get update && apt-get install -y gcc
RUN apt-get update && apt-get install -y gcc-multilib gdb-multiarch cmake make
RUN apt-get update && apt-get install -y python-dev python-pip python-setuptools

RUN pip install -U pip
RUN echo 'from pip import main' > /usr/bin/pip
RUN echo 'if name == 'main':' >> /usr/bin/pip
RUN echo ' sys.exit(main._main())' >> /usr/bin/pip

RUN apt-get update && pip install pwntools==3.5.0 ropgadget
RUN apt-get update && apt-get install -y gdb vim
RUN apt-get update && apt-get install -y git fish wget

RUN apt-get install zsh
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
RUN cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

RUN git clone https://github.com/longld/peda.git ~/peda
RUN wget -q -O ~/.gdbinit-gef.py https://github.com/hugsy/gef/raw/master/gef.py
RUN git clone git://github.com/Mipu94/peda-heap.git ~/peda-heap
RUN echo "source ~/peda/peda.py" >> ~/.gdbinit
RUN echo "source ~/peda-heap/peda.py" >> ~/.gdbinit
RUN apt-get install -y ruby gem
RUN gem sources --remove http://rubygems.org/ 
RUN gem sources --remove https://rubygems.org/ 
RUN gem sources -a https://gems.ruby-china.com/ 
RUN gem install one_gadget

RUN useradd -m ctf

WORKDIR /home/ctf

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

RUN mkdir /home/ctf/process
RUN chown -R root:ctf /home/ctf
RUN chmod -R 750 /home/ctf

EXPOSE 10000
