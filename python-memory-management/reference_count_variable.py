"""Python primarily uses Reference Counting and uses the Garbage Collector only to clean up cyclic references."""

import sys
x = []

y = x

print(sys.getrefcount(x)) # you see 3 because when x passes in getrefcount it create a temperary


class A:
    pass

a = A()
a.self = a #it reference itself if you delete object still refrence count is 1 so how it free it. GC find the cycle
print(id(a))
print(sys.getrefcount(a))
import gc
gc.collect()
