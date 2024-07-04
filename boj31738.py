import math
import sys

input = sys.stdin.readline

N ,M = input().split()

if int(N) < int(M) :
    print(math.factorial(int(N)) % int(M))
else :
    print(0)