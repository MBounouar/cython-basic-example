# Import the extension module hello.
import hello
import mview

import numpy as np

# Call the print_result method
print("using hello module ...\n")
hello.test_hello()
print("\n...Done using hello module\n")

print("using mview module ...\n")
# example taken from
# https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html
narr = np.arange(27, dtype=np.dtype("i")).reshape((3, 3, 3))
print("sum of NumPy array is %s" % mview.sum3d(narr))
print("\n...Done using mview module\n")
