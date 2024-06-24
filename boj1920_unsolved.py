from bisect import bisect_left
from sys import stdin

N = int(input())
N_list = list((map(int, stdin.readline().split())))
N_list.sort()

M = int(input())
M_list = list(map(int, stdin.readline().split()))

for i in M_list :
    if bisect_left(N_list, i) == N:
        print(0)
    else :
        print(1)
