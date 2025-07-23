# Specify the minimum required CMake version
cmake_minimum_required(VERSION 3.10)

project(pybind)

# Change the name of your lib
set(LIB_NAME my_custom_lib)

# Choose C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Output directory for .so file
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/output)

# Get all .cpp files from src directory
file(GLOB SRC_CPP_FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")

# Create library based on your .cpp files
add_library(${LIB_NAME} SHARED
    ${SRC_CPP_FILES}
)

# Directories to header (.h) files
target_include_directories(${LIB_NAME} PRIVATE
    src
    include
)

execute_process(COMMAND python3 -m pybind11 --includes
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE PYBIND11_INC
)

string(REPLACE " " ";" PYBIND11_INC "${PYBIND11_INC}")
message(STATUS "PYBIND11_INC: ${PYBIND11_INC}")

target_compile_options(${LIB_NAME} PRIVATE
    ${PYBIND11_INC}
)

# Get the suffix for .so file of your custom library
execute_process(COMMAND python3-config --extension-suffix
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE PYBIND11_SUFFIX
)

# Format name of .so file of your custom library
set_target_properties(${LIB_NAME} PROPERTIES
    OUTPUT_NAME ${LIB_NAME}${PYBIND11_SUFFIX}
    PREFIX "" SUFFIX ""
)

