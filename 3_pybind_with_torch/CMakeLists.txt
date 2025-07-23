# Specify the minimum required CMake version
cmake_minimum_required(VERSION 3.10)

project(pybind)

# Change the name of your lib
set(LIB_NAME my_custom_lib)

execute_process(COMMAND python3 -c "import torch; print(torch.compiled_with_cxx11_abi())"
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE TORCH_ABI
)

if (TORCH_ABI STREQUAL "True")
    set(cxx_abi 1)
else()
    set(cxx_abi 0)
endif()

message(STATUS "USE_CXX_ABI:${cxx_abi}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_GLIBCXX_USE_CXX11_ABI=${cxx_abi}")

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

# Get path to torch Python library: /path/to/site-packages/torch
execute_process(COMMAND python3 -c "import os; import torch; print(os.path.dirname(torch.__file__))"
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE TORCH_PATH
)

message(STATUS "TORCH_PATH: ${TORCH_PATH}")

# Get all .so files from src directory
file(GLOB TORCH_LIBRARIES ${TORCH_PATH}/lib/*.so)

target_link_libraries(${LIB_NAME}
    ${TORCH_LIBRARIES}
)

target_link_directories(${LIB_NAME} PRIVATE
    ${TORCH_PATH}/lib
)

# Directories to header (.h) files of used libraries (torch here as an example)
target_include_directories(${LIB_NAME} PRIVATE
    ${TORCH_PATH}/include
    ${TORCH_PATH}/include/torch/csrc/api/include
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
    -D_GLIBCXX_USE_CXX_ABI=${cxx_abi}
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
