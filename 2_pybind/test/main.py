import os
import sys 

# You need to ensure that os.getcwd()}/output is the directory with your .so file 
sys.path.insert(0, f'{os.getcwd()}/output')
# Import will be successfully only if .so file will be found
import my_custom_lib


def check(a, b):
    c_real = a + b
    print(f'Real result: {c_real}')

    # Be ready for Hello world message
    c_actual = my_custom_lib.add(a, b)
    print(f'Actual result: {c_actual}')


def main():
    check(1, 2)
    check(3.14, 2.17)


if __name__ == '__main__':
    main()
