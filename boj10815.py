import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
N_l = sorted(list(map(int, sys.stdin.readline().split())))
M = list(map(int, sys.stdin.readline().split()))
M_l = sorted(list(map(int, sys.stdin.readline().split())))

for i in M_l :
    if bisect_left(N_l, i) == N + 1 :
        print(0, end=' ')
    else :
        print(1, end=' ')
