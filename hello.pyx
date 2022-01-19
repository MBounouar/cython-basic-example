import cython
import numpy as np
cimport numpy as np

from libc.stdio cimport printf

cdef extern from "spam.h":
    void order_spam()
    print(a,b)

def test_hello():
    cdef int num_threads
    
    printf("Hello ")
    printf("World \n")
    return order_spam()
