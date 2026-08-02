"""Sometimes you want to point to an object

without increasing the reference count."""


"""Useful for

caches
observers
GUI frameworks
avoiding memory leaks"""

import weakref
import sys


class A:
    pass

a = A()
w = weakref.ref(a)
print(a)
print(w)
print(sys.getrefcount(a))
