#!/bin/python3

import sys

even = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if a % 2 == 0:
        even.append(a)
    print(sum(even))
