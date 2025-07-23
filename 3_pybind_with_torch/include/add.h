#ifndef ADD_H
#define ADD_H

#include "torch/extension.h"

at::Tensor custom_add(at::Tensor a, at::Tensor b);

#endif // ADD_H