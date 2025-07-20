# Specify the minimum required CMake version
cmake_minimum_required(VERSION 3.10)

project(run_cpp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Change the name of executable file
set(EXECUTABLE_NAME cmake_example)

# Change the directory for executable file
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/output)

# Get all .cpp files from src directory
file(GLOB CPP_SOURCES src/*.cpp)

# Step 1: Create executable file based on .cpp files
add_executable(${EXECUTABLE_NAME}
    ${CPP_SOURCES}
)

# Step 2: Add path to directories with header files
target_include_directories(${EXECUTABLE_NAME} PRIVATE
    ${CMAKE_SOURCE_DIR}/include
)
