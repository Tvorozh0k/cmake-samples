# Compilation stage
mkdir -p build && cd build
cmake ..
make

# Execution stage
cd ..
python test/main.py
