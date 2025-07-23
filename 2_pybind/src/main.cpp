#include <pybind11/pybind11.h>

#include "hello.h"
#include "add.h"

template <typename T>
T example (T a, T b) {
    hello();
    return custom_add(a, b);
}

PYBIND11_MODULE(my_custom_lib, m) {
    m.doc() = "PyBind Example";

    // Note: the name for python method may differ from the name of c++ method
    // Note: overloading support!
    m.def("add", &example<int>, "The sum of two integers");
    m.def("add", &example<float>, "The sum of two float values");
}
