#include <pybind11/pybind11.h>

#include "hello.h"
#include "add.h"

at::Tensor example(at::Tensor a, at::Tensor b) {
    hello();
    return custom_add(a, b);
}

PYBIND11_MODULE(my_custom_lib, m) {
    m.doc() = "PyBind Example";

    // Note: the name for python method may differ from the name of c++ method
    m.def("add", &example, "The sum of two tensors");
}
