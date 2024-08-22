#! /bin/bash
n_proc=$1

cd gem5/ext/ramulator2/ramulator2
mkdir build
cd build
cmake ..
make -j ${n_proc}
cp ./ramulator2 ../ramulator2
cd ../../../../
scons build/X86/gem5.opt -j ${n_proc}
