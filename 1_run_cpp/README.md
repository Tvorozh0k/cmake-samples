## 1. Overview

This project is about execution of C++ code using CMake.

## 2. Directory structure

```
1_run_cpp
│   README.md
│   CMakeLists.txt
│   run.sh
│
└───include
│   │   hello.h
│   
└───src
│   │   hello.cpp
│   │   main.cpp
│
└───build (after compilation)
│   │   ...
│
└───output (after compilation)
    │   cmake_example
```

> Note: `build` and `output` directories will appear only after `run.sh` script execution

* `include` folder contains all necessary header (.h) files. All realizations (.cpp files) are in `src` folder

## 3. Run code

To run this code use `run.sh` script:

```
# chmod +x ./run.sh (if run.sh doesn't 
# have rights to be executable)
./run.sh
```

* During compilation `build` and `output` directories will be generated. In `output` folder there will be your executable file (e.g. `cmake_example`)

* Run `./output/cmake_example` after CMake compilation if you don't want to do some changes in your C++ code (just execute this code for once again)

* Run `run.sh` every time, when you need to do some changes in your C++ code