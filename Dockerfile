FROM ghcr.io/gem5/ubuntu-22.04_all-dependencies:v23-0
LABEL creator="mainpower4309@gmail.com"
LABEL version="1.0.0"

#ARG DEBIAN_FRONTEND=noninteractive
#ENV TZ=America/New_York
#ENV PYTHONIOENCODING=UTF-8
#ENV LC_CTYPE=C.UTF-8v

USER root
WORKDIR /root

RUN apt-get update 
RUN apt-get install build-essential -y
RUN apt-get install git -y
RUN apt-get install c++-12 -y
RUN apt-get install clang clang++-15 -y
RUN apt-get install cmake -y
 
RUN git clone https://github.com/sangjae4309/gem5-ramulator2.git /root/gem5-ramulator2
RUN git clone https://github.com/gem5/gem5.git /root/gem5-ramulator2/gem5
RUN cd /root/gem5-ramulator2/gem5 && git reset --hard 48a40cf2f5182a82de360b7efa497d82e06b1631
RUN mkdir /root/gem5-ramulator2/gem5/ext/ramulator2 
RUN git clone https://github.com/CMU-SAFARI/ramulator2.git /root/gem5-ramulator2/gem5/ext/ramulator2/ramulator2
RUN cd /root/gem5-ramulator2/gem5/ext/ramulator2/ramulator2 && git reset --hard 0eafaa4c3df7b333f8645f1249afa52390c89616


RUN chmod -R 755 /root/gem5-ramulator2/wrapper/mem/*
RUN chmod -R 755 /root/gem5-ramulator2/wrapper/common/*
RUN chmod -R 755 /root/gem5-ramulator2/wrapper/SConscript 

RUN cp /root/gem5-ramulator2/wrapper/mem/* /root/gem5-ramulator2/gem5/src/mem
RUN cp /root/gem5-ramulator2/wrapper/common/* /root/gem5-ramulator2/gem5/configs/common
RUN cp /root/gem5-ramulator2/wrapper/SConscript /root/gem5-ramulator2/gem5/ext/ramulator2
RUN cp /root/gem5-ramulator2/wrapper/python/SConscript /root/gem5-ramulator2/gem5/src/python/
RUN cp /root/gem5-ramulator2/wrapper/python/ramulator_2.py /root/gem5-ramulator2/gem5/src/python/gem5/components/memory



