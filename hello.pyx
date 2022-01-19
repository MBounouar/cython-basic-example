import cython
import numpy as np
cimport numpy as np

from libc.stdio cimport printf

cdef extern from "spam.h":
    void order_spam()

def test_hello():
    printf("Hello ")
    printf("World \n")
    return order_spam()
