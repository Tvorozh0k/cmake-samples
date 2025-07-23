import os
import sys 

import torch

# You need to ensure that os.getcwd()}/output is the directory with your .so file 
sys.path.insert(0, f'{os.getcwd()}/output')
# Import will be successfully only if .so file will be found
import my_custom_lib

# It even works for device='cuda' (wow)!
a = torch.rand((3, 3), dtype=torch.float16, device='cpu')
b = torch.rand((3, 3), dtype=torch.float16, device='cpu')

print(f'Tensor a:\n{a}')
print(f'Tensor b:\n{b}')

c_real = a + b
print(f'Torch result:\n{c_real}')

# Be ready for Hello world message
c_actual = my_custom_lib.add(a, b)
print(f'Custom lib result:\n{c_actual}')

# Calculate MSE
diff = torch.abs(c_real - c_actual).square().mean()

if diff < 1e-5:
    print('Test pass!')
else:
    print('Test failed:')
    print(f'Real result:\n{c_real}')
    print(f'Actual result:\n{c_actual}')
