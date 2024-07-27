FROM ubuntu:22.04 
LABEL creator="mainpower4309@gmail.com"
LABEL version="1.0.0"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ America/New_York
ENV PYTHONIOENCODING UTF-8
ENV LC_CTYPE C.UTF-8

USER root
WORKDIR /root

RUN apt-get update 
RUN apt-get install build-essential -y
RUN apt-get install git -y
RUN apt-get install c++-12 -y
RUN apt-get install clang clang++-15 -y

RUN git clone https://github.com/sangjae4309/gem5-ramulator2.git /root/gem5-ramulator2
RUN git clone https://github.com/gem5/gem5.git /root/gem5-ramulator2/gem5
RUN mkdir /root/gem5-ramulator2/gem5/ext/ramulator2 
RUN git clone https://github.com/CMU-SAFARI/ramulator2.git /root/gem5-ramulator2/gem5/ext/ramulator/ramulator2


RUN chmod -R 755 /root/gem5-ramulator2/mem/*
RUN chmod -R 755 /root/gem5-ramulator2/common/*
RUN chmod -R 755 /root/gem5-ramulator2/ramulator2_tmp/SConscript 

RUN cp /root/gem5-ramulator2/mem/* /root/gem5-ramulator2/gem5/src/mem
RUN cp /root/gem5-ramulator2/common/* /root/gem5-ramulator2/gem5/src/mem
RUN cp /root/gem5-ramulator2/ramulator2_tmp/SConscript /root/gem5-ramulator2/gem5/ext/ramulator2/ramulator2



