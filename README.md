## Enviorment
- \>= Ubuntu22.04 (due to support on c++23)
- c++-12 (apt-get install c++-12)
- clang++-15 (apt-get install clang clang++-15)
- cmake
- gem5 ver.230830

## Guide
- move files as follows:
  - `./mem/*` --> `gem5/src/mem`
  - `./common/*` --> `gem5/configs/common`
  - `./ramulator2_tmp/Sconscript` --> `gem5/ext/ramulator2/ramulator2`
- The detail explanation is available at [docs_ramulator2](https://sangjae4309.github.io/docs_ramulator2/index.html)
- The example of configuration file and command is `./example`
