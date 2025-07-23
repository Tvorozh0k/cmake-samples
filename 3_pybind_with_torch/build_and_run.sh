# Compilation stage
mkdir -p build && cd build
cmake ..
make

# Execution stage
cd ..
# [Optional] conda environment has its own GLIBC which might be too old for
# the system gcc version. Use LD_PRELOAD with the path to system GLIBC 
# to use system version of GLIBC and avoid such a problem
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python test/main.py