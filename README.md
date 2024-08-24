# Integrating gem5 + Ramulator2

## Introduction
This repository distributes a enviorment that integrates gem5 and ramulator2.

The The repository contains following contents and files

- `mem/`: contains a ramulator2 wrapper and config file. transfer files to `gem5/src/mem`
- `common/`: contains a option file. transfer files to `gem5/configs/common`
- `ramulator2_tmp/`: contains a Sconscript to include ramultor2 in compiling. transfer files to `gem5/ext/ramulator2/
- `example/`: example scripts and binary file to test.
- example/mcf_only_4core_example.cmd shows an example of running mcf, one of benchmark in SPEC2006.
- The detail about what the files do can be seen on [How to integerate Ramulator2 to gem5](https://sangjae4309.github.io/docs-gem5/external_simulator/ramulator2).

## Getting started
Clone the repository (don't need to include `--recursive`)
```
git clone https://github.com/sangjae4309/gem5-ramulator2.git
```

First, you need base image provided from [gem5 official](https://www.gem5.org/documentation/general_docs/building). This repo uses ubuntu22.04.
```
docker pull ghcr.io/gem5/ubuntu-22.04_all-dependencies:v23-0
```

Then build new docker images wit pre-defined `Dockerfile` (It takes a while to end) and execute the image
```
docker build --tag gem5-ramulator2 .
docker run -d -it --name gem5-ramulator2 gem5-ramulator2:latest
docker exec -it gem5-ramulator2 /bin/bash
```

After attached to `gem5-ramulator2` container, run pre-defined build script which automatically compile Ramulator2 and gem5. The first argument means number of core your machine will use
```
cd gem5-ramulator2
./build 4
```

Test simple binary file which runs matrix multiplication
```
cd gem5
build/X86/gem5.opt configs/deprecated/example/se.py --cmd=tests/test-progs/hello/bin/x86/linux/hello --cpu-type=TimingSimpleCPU --l1d_size=64kB --l1i_size=16kB --caches --mem-type=Ramulator2 --ramulator-config=../example/DDR4.yaml --cmd=../example/mm_base
```
