from bisect import bisect_left
import sys

N = int(input())
N_list = list((map(int, sys.stdin.readline().split())))
N_list.sort()

M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))
M_list.sort()

for i in M_list :
    if bisect_left(N_list, i) == len(N_list) + 1 :
        print(0)
    else :
        print(1)