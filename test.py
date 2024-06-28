import collections
import sys

A = collections.deque([1,2,3,4,5])
A.rotate(len(A)//2)

print(A)
