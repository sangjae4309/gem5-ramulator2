## Integrating gem5 + Ramulator2

This repository distributes a enviorment that integrates gem5 and ramulator2.
The repository contains following contents and files

- `mem/`: contains a ramulator2 wrapper and config file. transfer files to `gem5/src/mem`
- `common/`: contains a option file. transfer files to `gem5/configs/common`
- `ramulator2_tmp/`: contains a Sconscript to include ramultor2 in compiling. transfer files to `gem5/ext/ramulator2/
- `example/`: example scripts to run gem5.
- example/mcf_only_4core_example.cmd shows an example of running mcf, one of benchmark in SPEC2006.
- The detail about what the files do can be seen on [How to integerate Ramulator2 to gem5](https://sangjae4309.github.io/docs-gem5/external_simulator/ramulator2).

## Enviorment
- Because ramualtor2 is based on c++23, the following enviorment is required
   - Ubuntu22.04
   - c++-12 
   - clang++-15 
   - cmake
   - gem5 version 23.0.1
- For your convenience, We provide `Dockerfile` which already builds alll necessary enviorements. Just run the following commands;

```
docker build --tag gem5-ramulator2 .
docker run -d -it --name gem5-ramulator2 gem5-ramulator2:latest
docker exec -it gem5-ramulator2 /bin/bash
```

